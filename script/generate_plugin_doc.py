from dataclasses import dataclass
import os
import sys
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import re
import textwrap
# cd script
# python3 generate_plugin_doc.py ../../dfir-ogre-plugin-windows/configuration/ ../content/
class FieldRow:
    """Simple container for one markdown table row."""

    def __init__(
        self,
        output_name: str,
        data_type: str,
        qualifier: str,
        description: str,
        parents: "List[Field]",
    ):
        self.output_name = output_name
        self.data_type = data_type
        self.qualifier = qualifier
        self.description = description
        self.parents: List[Field] = parents

    def to_md(self) -> Optional[str]:
        """Return the row formatted as a markdown table line."""
        name = ""
        for parent in self.parents:
            if parent.output_name:
                name += parent.output_name
                if parent.data_type.startswith("Array["):
                    name += "[]"
                name += "."

        name += self.output_name
        if self.data_type.startswith("Array["):
            name += "[]"

        return (
            f"| `{name}` | {self.data_type} | {self.qualifier} | {self.description} |"
        )


class Field:
    def __init__(
        self, output_name: str, data_type: str, qualifier: str, description: str
    ):
        self.output_name = output_name
        self.data_type: str = data_type
        self.qualifier: str = qualifier
        self.description: str = description
        self.children: List[Field] = []

    def flatten(self, parent_list: "List[Field]") -> List[FieldRow]:
        rows: List[FieldRow] = []
        parents = parent_list.copy()
        if self.output_name:
            row = FieldRow(
                self.output_name,
                self.data_type,
                self.qualifier,
                self.description,
                parent_list.copy(),
            )
            rows.append(row)

        parents.append(self)

        for child in self.children:
            childs = child.flatten(parents)
            rows.extend(childs)
        return rows


def parse_field_elem(elem: ET.Element, parent_field: Field):
    def _name(e: ET.Element) -> Optional[str]:
        return e.attrib.get("output") or e.attrib.get("input")

    parser = elem.attrib.get("parser")
    if parser == "Ignore":
        return  # skip ignored fields entirely

    if elem.tag == "field":
        # If the field contains child <field>/<object>/<array>, treat it as a
        # container and recurse on the children (do not emit a row for it).
        if any(child.tag in ("field", "object", "array") for child in elem):
            for child in elem:
                parse_field_elem(child, parent_field)

                # Determine the base name for this field
        field_name = _name(elem)
        if not field_name:
            return  # no name → ignore

        qualifier = elem.attrib.get("qualifier", "")
        description = elem.attrib.get("description", "")
        if parser:
            parent_field.children.append(
                Field(field_name, parser, qualifier, description)
            )

    elif elem.tag == "object":
        obj_name = _name(elem)
        if not obj_name:
            return  # no name → ignore
        qualifier = elem.attrib.get("qualifier", "")
        description = elem.attrib.get("description", "")
        object_field = Field(obj_name, "Object", qualifier, description)
        for child in elem:
            parse_field_elem(child, object_field)
        parent_field.children.append(object_field)

    elif elem.tag == "array":
        child = None
        for sub_elem in elem:
            child = sub_elem

        if child is not None:
            dummy_field = Field("", "", "", "")
            parse_field_elem(child, dummy_field)
            field = dummy_field.children.pop()

            field.data_type = f"Array[{field.data_type}]"
            parent_field.children.append(field)


def parse_description(
    root: ET.Element,
    plugin: Optional[str],
    data_type: Optional[str],
) -> str:
    """
    create a Description section
    """
    md = "\n\n"
    md += """{{< callout type="important" >}}"""
    md += f"Data Type: **{data_type}** \\\n"
    md += f"\tPython Parser: **{plugin}**"
    md += "{{< /callout >}}\n\n"
    md += "### Description \n\n"
    descr = root.find(".//description")
    if descr is not None and descr.text is not None:
        md += descr.text.strip()
        md += "\n\n"

    return md


def parse_timeline(root: ET.Element) -> str:
    """
    Parse the <timeline> section of the given XML configuration file
    """
    timeline_elem = root.find("./timeline")

    if timeline_elem is None:
        return """{{< callout type="warning" >}}This plugin does not contains timestamped data and cannot be used to create a timeline{{< /callout >}}"""

    related_user = timeline_elem.find("./related_user")
    rows: List[Tuple[str, str]] = []
    if related_user is not None:
        for out_elem in related_user.findall("./output_name"):
            value = out_elem.get("value")
            if value:
                rows.append(("Related User", value))

    description = timeline_elem.find("./description")
    first_decr = True
    if description is not None:
        for out_elem in description.findall("./output_name"):
            value = out_elem.get("value")
            if value:
                if first_decr:
                    rows.append(("Description", value))
                else:
                    rows.append(("", value))
            first_decr = False

    additional_description = timeline_elem.find("./additional_description")
    first_decr = True
    if additional_description is not None:
        for out_elem in additional_description.findall(".//output_name"):
            value = out_elem.get("value")
            if value:
                if first_decr:
                    rows.append(("Additional Description", value))
                else:
                    rows.append(("", value))
            first_decr = False

    md = "| Timeline Field | Data Field |\n"
    md += "|---|---|\n"
    for row in rows:
        md += f"|{row[0]}    | `{row[1]}`   |\n"
    return md


def parse_fields(root: ET.Element) -> str:
    """
    Parse the <fields> section of the given XML configuration file
    and return a list of Row objects ready for markdown rendering.
    """

    # Find the first <fields> element under the mapping – there is exactly one.
    fields_elem = root.find("./fields")
    if fields_elem is None:
        raise ValueError(f"No <fields> element found in {root}")

    root_field = Field("", "", "", "")
    for child in fields_elem:
        parse_field_elem(child, root_field)

    rows = root_field.flatten([])
    md = "| Output Name | Data Type | Qualifier | Description |\n"
    md += "|---|---|---|---|\n"
    for row in rows:
        serialized = row.to_md()
        if serialized:
            md += serialized + "\n"

    return md


PLUGIN_FOLDER = "Built-in Plugins"


# python3 generate_plugin_doc.py ../../dfir-ogre-plugin/configuration/ ../content/
def main() -> None:
    if len(sys.argv) != 3:
        print(
            "Usage: python3 generate_plugin_doc.py <path/to/configuration/folder> <path/to/documentation/folder>"
        )
        sys.exit(1)

    configuration_folder = Path(sys.argv[1])
    doc_path = Path(sys.argv[2])
    doc_folder = init_doc_folder(doc_path, PLUGIN_FOLDER)
    api_tree = APITree()
    config_files = list_files_in_directory(configuration_folder)
    for xml_file in config_files:
        print(xml_file)
        tree = ET.parse(str(xml_file))
        root = tree.getroot()
        parser = root.get("parser", "")

        mappings = root.findall("./mapping")

        for mapping in mappings:
            data_type = mapping.get("data_type")
            if data_type is None:
                continue

            category = mapping.find("./category")
            cat_text = ""
            if category is not None and category.text is not None:
                cat_text = category.text

            description = mapping.find("./description")
            descr_text = ""
            if description is not None and description.text:
                descr_text = description.text.split(".")[0]

            md = parse_description(mapping, parser, data_type)
            md += "\n### Timeline \n\n"
            md += parse_timeline(mapping)
            md += "\n### Fields \n\n"
            md += parse_fields(mapping)

            doc = Document(parser, data_type, cat_text, descr_text, md)
            api_tree.add(doc)
            # print(md)

        api_tree.write_doc(doc_folder)


def init_doc_folder(doc_folder: Path, root_folder) -> str:
    base_folder = os.path.join(doc_folder, root_folder)
    shutil.rmtree(base_folder)
    os.makedirs(base_folder)
    return base_folder


@dataclass
class Document:
    parser: str
    data_type: str
    category: str
    description: str
    content: str


class APITree:
    map: Dict[str, List[Document]]

    def __init__(self):
        self.map = {}

    def add(self, document: Document):
        if document.category not in self.map:
            self.map[document.category] = []
        self.map[document.category].append(document)

    def write_doc(self, folder_path: str):
        every_cards: List[Card] = []
        link_set = set()
        for folder, docs in self.map.items():
            doc_folder_path = os.path.join(folder_path, folder)
            os.makedirs(doc_folder_path, exist_ok=True)
            cards: List[Card] = []
            for doc in docs:
                title = doc.data_type.replace("win_", "").replace("_", " ").title()
                link = doc.data_type
                if link in link_set:
                    last_parser_word = last_camel_case_word(doc.parser)
                    link += "_" + last_parser_word.lower()
                    title += " " + last_parser_word
                link_set.add(link)
                subtitle = doc.description.strip().replace("\n", " ")

                card = Card(doc.category, doc.parser, link, title, subtitle)
                cards.append(card)
                doc_path = os.path.join(doc_folder_path, f"{link}.md")
                with open(doc_path, "w") as text_file:
                    text_file.write("---\n")
                    text_file.write(f" title: '{title}'\n")
                    text_file.write("---\n")
                    text_file.write(doc.content)

            index_path = os.path.join(doc_folder_path, "_index.md")
            cards.sort(key=lambda x: x.title, reverse=False)
            with open(index_path, "w") as index_file:
                index_file.write("---\n")
                index_file.write(f" title: '{folder}'\n")
                index_file.write("---\n")



                index_file.write("{{< cards >}}\n")
                for card in cards:
                    index_file.write(f"{card.get_parser_card()}\n")
                index_file.write("{{< /cards >}}\n")
            every_cards.extend(cards)

        plugin_index_path = os.path.join(folder_path, "_index.md")
        with open(plugin_index_path, "w") as index_file:
            index_file.write("---\n")
            index_file.write(f" title: '{PLUGIN_FOLDER}'\n")
            index_file.write(" weight: 3\n")
            index_file.write("---\n")

            index_file.write(textwrap.dedent("""
            DFIR-OGRE provides a collection of plug‑ins, each dedicated to parsing a specific class of Windows artefacts. The built‑in plug‑ins cover a lot of artefacts that appears in a typical DFIR-ORC archive.

            ## Retrieving the plugins

            Plugins can be retrieved by cloning the `dfir-ogre-plugin-windows` repository

            ```bash
            # Choose a location where you keep all the sources
            mkdir -p ~/dfir-ogre && cd ~/dfir-ogre

            git clone https://github.com/ANSSI-FR/dfir-ogre-plugin-windows.git
            ```

            The plugins are located in dfir-ogre-plugin-windows/configuration folder

            ---

            ## Plugin list

            """))



            index_file.write("{{< cards >}}\n")
            every_cards.sort(key=lambda x: x.title, reverse=False)
            for card in every_cards:
                index_file.write(f"{card.get_category_card()}\n")
            index_file.write("{{< /cards >}}\n")


BADGE_COLORS: Dict[str, str] = {}


@dataclass
class Card:
    category: str
    parser: str
    link: str
    title: str
    subtitle: str

    def get_parser_card(self) -> str:
        tag = Card.shorten_parser(self.parser)
        color = Card.get_category_color(tag)
        card = " {{"
        card += f"""< card link="{self.link}" title="{self.title}" subtitle="{self.subtitle}" tag="{tag}" tagColor="{color}">"""
        card += "}}"

        return card

    def get_category_card(self) -> str:
        color = Card.get_category_color(self.category)
        category = self.category.lower().replace(" ", "-")
        card = " {{"
        card += f"""< card link="{category}/{self.link}" title="{self.title}" subtitle="{self.subtitle}" tag="{self.category}" tagColor="{color}">"""
        card += "}}"

        return card

    @classmethod
    def get_category_color(cls, category: str) -> str:
        if category not in BADGE_COLORS:
            BADGE_COLORS[category] = ColorPicker.pick()
        return BADGE_COLORS[category]

    @classmethod
    def shorten_parser(cls, category: str) -> str:
        if category.startswith("Reg"):
            return "Registry"
        return category


class ColorPicker:
    colors = [
        "purple",
        "indigo",
        "blue",
        "green",
        "yellow",
        "amber",
        "orange",
        "red",
        "gray",
    ]
    position = 0

    @classmethod
    def pick(cls) -> str:
        color = cls.colors[cls.position]
        cls.position += 1
        if cls.position >= len(cls.colors):
            cls.position = 0
        return color


def build_root_badges(): ...


def list_files_in_directory(directory: Path) -> List[str]:
    file_list: List[str] = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))

    return file_list


def last_camel_case_word(str: str) -> str:
    return re.findall(r"[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))", str).pop()


if __name__ == "__main__":
    main()
