---
date: '2026-01-06T15:54:09+01:00'
title: 'XML plugin'
cascade:
  type: docs
  params:
    breadcrumbs: true
weight: 4
---

A guides to create a plugin that parses XML files.

It is not as detailled that the [CSV tutorial](/plugin-creation/generic_plugins/csv_tutorial/) and focus on the specific features.
It also introduces more complex field types to hanlde `arrays` and `objects`.

## Sample Dataset
Before starting, let's create our sample XML file :

```xml {filename="library.xml"}
<?xml version="1.0" encoding="UTF-8"?>
<library name="my library">
    <book id="b1">
        <title>Programming Rust</title>
        <authors>
            <author>Blandy Shannon</author>
            <author>Doe John</author>
        </authors>
        <versions>
            <version value="1" year="2017">first version</version>
        </versions>
        <description>
            <short>Programming Lorem ipsum </short>
            <summary>Programming Lorem ipsum dolor sit amet</summary>
        </description>
    </book>
    <book id="b2">
        <title>Rust in Action</title>
        <authors>
            <author>McNamara Tim</author>
            <author>Doe Jeanne</author>
        </authors>
        <versions>
            <version value="1" year="2021">first version</version>
            <version value="2" year="2025">second version</version>
        </versions>
        <description>
            <short>Lorem ipsum Action</short>
            <summary>Action Lorem ipsum dolor sit amet</summary>
        </description>
    </book>
</library>
```
We will create a plugin that extracts one artefact per book.

## XML Descriptor

```xml {filename="configuration/library_plugin.xml"}
<?xml version="1.0" encoding="UTF-8" ?>
<plugin parser="XML" file_encoding="UTF_8">
  <mapping data_type="library">
    <description>Parse books from a library xml file</description>
    <xpath_tuple value="/library/book" />
    <fields>
      <field input="../@name" output="library" parser="String" />
      <field input="@id" output="id" parser="String" />
      <field input="title" output="title" parser="String" />
      <array>
        <field input="authors/author" output="authors" parser="String" />
      </array>
      <array>
        <object input="versions/version" output="versions">
          <field input="@value" output="version" parser="String" />
          <field input="@year" output="year" parser="String" />
          <field input="." output="title" parser="String" />
        </object>
      </array>
      <object input="description" output="description">
        <field input="short" output="short" parser="String" />
        <field input="summary" output="summary" parser="String" />
      </object>
    </fields>
  </mapping>
</plugin>
```
Key points:
- `<plugin parser="XML" >`: the plugin uses the `XML`python parser.
- `<xpath_tuple value="/library/book" />` : defines the root path of an artefact. This **XPath** query will create two book artefacts.
- `<field input="../@name"`: input are defined as **XPath** query, this one will read the parent element an take the value of the `name` attribute ("my library")

To parse the `authors` list, we use the `<array>` element that will contains a list of String
```xml
<array>
  <field input="authors/author" output="authors" parser="String" />
</array>
```

The `versions` is more complex as in contains mutiple values. We create an `<array>` of `<object>` to handle the parsing. 
```xml
<array>
  <object input="versions/version" output="versions">
    <field input="@value" output="version" parser="String" />
    <field input="@year" output="year" parser="String" />
    <field input="." output="title" parser="String" />
  </object>
</array>
```

You can test the plugin with the following command. 
```bash
dfir-ogre plugin \
    --filename library.xml \
    --plugin_config configuration/library_plugin.xml \
    --computer_name SAMPLE_HOST \
    --output_folder output
```
