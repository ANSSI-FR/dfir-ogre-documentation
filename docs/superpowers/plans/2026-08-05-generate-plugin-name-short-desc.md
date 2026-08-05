# Rework `generate_plugin_doc.py` to Use `<name>` + `<short_description>`

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `dfir-ogre-documentation/script/generate_plugin_doc.py` produce page titles and file/link names from each mapping's `<name>`, and card subtitles from `<short_description>`, removing the old `data_type`-based mangling and disambiguation.

**Architecture:** Edit the single standalone script `generate_plugin_doc.py` and its helper classes so that `Document` carries the `<name>` and `<short_description>`, `Document.name` becomes the display title and the file link (via a new `slugify_name` helper slugging to lowercase-with-underscores), and the cards use the short description as subtitle. Delete the now-unneeded `link_set`/`last_camel_case_word`/title-mangling logic and add a defensive slug-uniqueness guard. Because the script is a standalone Hugo tool with no existing test harness, each task verifies pure helpers with a temporary inline `python3 -c` assertion and verifies generated output by running the script against a copy of the real configuration folder.

**Tech Stack:** Python 3, `xml.etree.ElementTree`, `pathlib`/`os`, `re` (already used by the script). No new dependencies.

## Global Constraints

- File name / link = lowercase, non-alphanumeric run `-> _`, trimmed. Example: `Chrome Download History` -> `chrome_download_history`.
- Display title = raw `<name>` (verbatim, no case mangling).
- Card subtitle = `<short_description>` (with newlines collapsed to spaces).
- `data_type` + `parser` still shown in the "Data Type / Python Parser" callout (`parse_description` output) — unchanged.
- Long `<description>` still rendered in the page body — unchanged.
- Category grouping, `_index.md`, and fields/timeline parsing unchanged.
- All work happens in `script/generate_plugin_doc.py`. Do not create a test framework or modify content except in Task 4 (regenerate checked-in docs).

---

### Task 1: Add `slugify_name` helper + uniqueness guard

**Files:**
- Modify: `script/generate_plugin_doc.py` (add `slugify_name`, add `resolve_link` uniqueness helper)
- Test: none committed; verify inline (repo has no test harness)

**Interfaces:**
- `slugify_name(name: str) -> str`
- `resolve_link(candidate: str, used_links: set) -> str`
- Produces: `slugify_name` and `resolve_link` used by Task 3's `write_doc`.

- [ ] **Step 1: Verify the intended behavior of the new helper with inline assertions**

Run:
```bash
cd /home/asalais/dev/dfir-ogre/dfir-ogre-documentation && python3 - <<'EOF'
import re
def slugify_name(name):
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
cases = {
    "Chrome Download History": "chrome_download_history",
    "Processes Orc V1": "processes_orc_v1",
    "X509Cert Software": "x509cert_software",
    "Prefetch": "prefetch",
    "CLSID Users": "clsid_users",
    "  User  Assist  ": "user_assist",
}
for name, expected in cases.items():
    got = slugify_name(name)
    assert got == expected, f"{name!r}: got {got!r}, want {expected!r}"
print("slugify_name OK")
EOF
```
Expected: prints `slugify_name OK`.

- [ ] **Step 2: Add the `slugify_name` and `resolve_link` helpers to the script**

In `script/generate_plugin_doc.py`, add right after the existing `last_camel_case_word` function (near the bottom, before `if __name__ == "__main__":`):

```python
def slugify_name(name: str) -> str:
    """Lowercase the name and convert every run of non-alphanumerics to one '_'."""
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def resolve_link(candidate: str, used_links: "set[str]") -> str:
    """Return a link derived from candidate that is unique within used_links.

    If candidate is taken, append a number; never silently overwrite an existing link.
    """
    link = candidate
    n = 2
    while link in used_links:
        link = f"{candidate}-{n}"
        n += 1
    used_links.add(link)
    return link
```

(Note: `last_camel_case_word` will be removed in Task 3; do not depend on it here.)

- [ ] **Step 3: Verify the helpers load**

Run:
```bash
cd /home/asalais/dev/dfir-ogre/dfir-ogre-documentation && python3 - <<'EOF'
import importlib.util
spec = importlib.util.spec_from_file_location("gen", "script/generate_plugin_doc.py")
gen = importlib.util.module_from_spec(spec); spec.loader.exec_module(gen)
assert gen.slugify_name("Foo Bar") == "foo_bar"
assert gen.resolve_link("a", {"a"}) == "a-2"
assert gen.resolve_link("b", {"b", "b-2"}) == "b-3"
assert gen.resolve_link("x", set()) == "x"
print("helpers OK")
EOF
```
Expected: prints `helpers OK`.

- [ ] **Step 4: Commit**

```bash
cd /home/asalais/dev/dfir-ogre/dfir-ogre-documentation && git add script/generate_plugin_doc.py && git commit -m "feat(script): add slugify_name and resolve_link helpers"
```

---

### Task 2: Carry `name` and `short_description` through `Document`/`main`

**Files:**
- Modify: `script/generate_plugin_doc.py` (`Document` dataclass, `main()`)

**Interfaces:**
- `Document(parser: str, data_type: str, category: str, name: str, subtitle: str, content: str)`
- Consumes: nothing new.
- Produces: `Document.name` (the display title) and `Document.subtitle` (the card subtitle), consumed by Task 3's `write_doc`.

- [ ] **Step 1: Update the `Document` dataclass and `main()`**

Current:
```python
@dataclass
class Document:
    parser: str
    data_type: str
    category: str
    description: str
    content: str
```
Replace with:
```python
@dataclass
class Document:
    parser: str
    data_type: str
    category: str
    name: str
    subtitle: str
    content: str
```

In `main()`, inside the `for mapping in mappings:` loop, after computing `cat_text`, read the new fields and replace the `Document(...)` construction, and the `subtitle`/`md` assembly. Replace the existing block:

```python
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
```

with:

```python
            category = mapping.find("./category")
            cat_text = ""
            if category is not None and category.text is not None:
                cat_text = category.text

            name_elem = mapping.find("./name")
            name = (
                name_elem.text.strip()
                if name_elem is not None and name_elem.text
                else data_type
            )

            short_elem = mapping.find("./short_description")
            subtitle = ""
            if short_elem is not None and short_elem.text:
                subtitle = short_elem.text.replace("\n", " ").strip()

            md = parse_description(mapping, parser, data_type)
            md += "\n### Timeline \n\n"
            md += parse_timeline(mapping)
            md += "\n### Fields \n\n"
            md += parse_fields(mapping)

            doc = Document(parser, data_type, cat_text, name, subtitle, md)
            api_tree.add(doc)
```

(`parse_description` still reads the long description itself, so the old `descr_text` first-sentence logic is dropped.)

- [ ] **Step 2: Verify the script still runs end-to-end without crashing**

Run on a throwaway output dir so we don't touch checked-in content:
```bash
cd /home/asalais/dev/dfir-ogre/dfir-ogre-documentation && rm -rf /tmp/docgen-out && python3 script/generate_plugin_doc.py /home/asalais/dev/dfir-ogre/dfir-ogre-plugin-windows/configuration /tmp/docgen-out && ls "/tmp/docgen-out/Built-in Plugins" && echo OK
```
Expected: prints the category subfolders and `OK`. (Output may still look old until Task 3.)

- [ ] **Step 3: Commit**

```bash
git add script/generate_plugin_doc.py && git commit -m "feat(script): carry name and short_description in Document"
```

---

### Task 3: Use `name`/`short_description` for titles, links, cards; remove old logic

**Files:**
- Modify: `script/generate_plugin_doc.py` (`APITree.write_doc`)

**Interfaces:**
- Consumes: `Document.name`, `Document.subtitle`, `slugify_name`, `resolve_link` (all defined above).
- Produces: correct `.md` files, `_index.md` cards, and root `_index.md` cards.

- [ ] **Step 1: Rewrite `APITree.write_doc`**

Replace the body of `write_doc` from `def write_doc(self, folder_path: str):` through the end of the root `_index.md` writing block so that:

- A single `used_links = set()` is created once before the per-folder loop (links must be unique across the whole site, matching the old `link_set` scope).
- For each doc:
  - `link = resolve_link(slugify_name(doc.name), used_links)`
  - `title = doc.name`
  - `subtitle = doc.subtitle`
  - `card = Card(doc.category, doc.parser, link, title, subtitle)`
  - page file written to `os.path.join(doc_folder_path, f"{link}.md")` with the same front matter as before (` title: '<title>'` and a blank line before it) and the same `doc.content`.
- Per-folder `_index.md` and root `_index.md` card loops stay structurally the same (cards sorted by title, `get_parser_card()` / `get_category_card()`), but they use the updated `title`/`subtitle`.

Remove entirely: the `link_set` / `last_camel_case_word` disambiguation, `title = doc.data_type.replace("win_", "").replace("_", " ").title()`, the `title += " " + last_parser_word` line, and `if link in link_set:` linking.

Concretely, the per-doc block becomes:

```python
        for doc in docs:
            link = resolve_link(slugify_name(doc.name), used_links)
            title = doc.name
            subtitle = doc.subtitle

            card = Card(doc.category, doc.parser, link, title, subtitle)
            cards.append(card)
            doc_path = os.path.join(doc_folder_path, f"{link}.md")
            with open(doc_path, "w") as text_file:
                text_file.write("---\n")
                text_file.write(f" title: '{title}'\n")
                text_file.write("---\n")
                text_file.write(doc.content)
```

Remove the now-unused `last_camel_case_word` function (nothing else references it after this change).

- [ ] **Step 2: Verify generated pages use `<name>` for title and file name**

Run:
```bash
cd /home/asalais/dev/dfir-ogre/dfir-ogre-documentation && rm -rf /tmp/docgen-out && python3 script/generate_plugin_doc.py /home/asalais/dev/dfir-ogre/dfir-ogre-plugin-windows/configuration /tmp/docgen-out
echo "--- prefetch page title ---"
grep "title" "/tmp/docgen-out/Built-in Plugins/Services and Applications/prefetch.md"
echo "--- shared data_type now unique links (chrome/firefox download history) ---"
ls "/tmp/docgen-out/Built-in Plugins/Browser Artefacts" | grep -i history
echo "--- no 'Xml Xml' style titles remain ---"
grep -rl "Xml Xml\|Xml XML" /tmp/docgen-out || echo "no Xml Xml leftover"
```
Expected:
- `title: 'Prefetch'` in `prefetch.md`.
- Links like `chrome_download_history.md` and `firefox_download_history.md` exist (unique), not `browser_download_history` + mangled variant.
- `no Xml Xml leftover`.

- [ ] **Step 3: Verify the generated `_index.md` cards use name + short_description**

Run:
```bash
grep -o '{{< card link="services-and-applications/prefetch" title="[^"]*" subtitle="[^"]*"' "/tmp/docgen-out/Built-in Plugins/_index.md"
```
Expected: `title="Prefetch"` and `subtitle` matching the `<short_description>` of `prefetch.xml` (`Shows Windows Prefetch execution evidence with executable names, run counts, last-run times, loaded files, and volumes.`), i.e. NOT the first sentence of the long description (`Parses Windows Prefetch files to extract execution metadata...`).

- [ ] **Step 4: Verify full generation is deterministic and collision-free**

Run:
```bash
cd /home/asalais/dev/dfir-ogre/dfir-ogre-documentation && rm -rf /tmp/docgen-out /tmp/docgen-out2 && python3 script/generate_plugin_doc.py /home/asalais/dev/dfir-ogre/dfir-ogre-plugin-windows/configuration /tmp/docgen-out && python3 script/generate_plugin_doc.py /home/asalais/dev/dfir-ogre/dfir-ogre-plugin-windows/configuration /tmp/docgen-out2 && diff -r -q "/tmp/docgen-out/Built-in Plugins" "/tmp/docgen-out2/Built-in Plugins" >/dev/null && echo "deterministic OK"
echo "--- page count (excludes _index.md) ---"
find "/tmp/docgen-out/Built-in Plugins" -name "*.md" ! -name "_index.md" | wc -l
echo "--- no duplicate final file names within the whole tree ---"
find "/tmp/docgen-out/Built-in Plugins" -name "*.md" ! -name "_index.md" -printf "%f\n" | sort | uniq -d | grep -v _index || echo "no dup filenames"
```
Expected: `deterministic OK`, page count `85`, and `no dup filenames`.

- [ ] **Step 5: Commit**

```bash
git add script/generate_plugin_doc.py && git commit -m "refactor(script): derive titles, links and card subtitles from name and short_description"
```

---

### Task 4: Verify against the real checked-in content

**Files:**
- Modify: `content/Built-in Plugins/` (regenerate checked-in docs)

**Interfaces:**
- Consumes: everything from earlier tasks.

- [ ] **Step 1: Regenerate the real `content/Built-in Plugins` folder**

```bash
cd /home/asalais/dev/dfir-ogre/dfir-ogre-documentation && python3 script/generate_plugin_doc.py /home/asalais/dev/dfir-ogre/dfir-ogre-plugin-windows/configuration content/
git status --short content/Built-in\ Plugins | head -30
```
Expected: git shows renamed/recreated `.md` files (old `data_type` names replaced by `<name>` slugs) and updated `_index.md` files. Script exits 0.

- [ ] **Step 2: Confirm page count and no leftover old names**

```bash
cd /home/asalais/dev/dfir-ogre/dfir-ogre-documentation && find "content/Built-in Plugins" -name "*.md" ! -name "_index.md" | wc -l
echo "--- old mangled links should be gone ---"
grep -rl "amcache_program_xml_xml\|Xml Xml" "content/Built-in Plugins" || echo "clean"
```
Expected: `85` pages, and `clean`.

- [ ] **Step 3: Build the Hugo site (sanity)**

```bash
cd /home/asalais/dev/dfir-ogre/dfir-ogre-documentation && (hugo --disableKinds=taxonomy,taxonomyTerm 2>&1 | tail -20 || echo "hugo not installed; skipping build")
```
Expected: site builds with warnings only (broken internal links would appear as errors/warnings). If hugo is unavailable, run the manual link check instead.

Manual link check (always run):
```bash
cd /home/asalais/dev/dfir-ogre/dfir-ogre-documentation && python3 - <<'EOF'
import re, glob, os
cards = open("content/Built-in Plugins/_index.md").read()
links = re.findall(r'link="([^"]+)"', cards)
existing = set()
for f in glob.glob("content/Built-in Plugins/**/*.md", recursive=True):
    existing.add(os.path.relpath(f, "content/Built-in Plugins").replace("\\","/").replace(".md",""))
missing=[l for l in links if l not in existing]
print("broken:", missing if missing else "none")
EOF
```
Expected: `broken: none`.

- [ ] **Step 4: Commit**

```bash
git add content/Built-in\ Plugins && git commit -m "docs: regenerate built-in plugin pages from name and short_description"
```
</content>
