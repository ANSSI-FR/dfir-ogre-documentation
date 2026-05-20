---
date: '2026-01-06T15:54:09+01:00'
title: 'Regexp plugin'
cascade:
  type: docs
  params:
    breadcrumbs: true
weight: 2
---

A guides to create a plugin that parses a text file using a regular expression. 

It is not as detailled that the [CSV tutorial](/plugin-creation/generic_plugins/csv_tutorial/) and focus on the specific features

## Sample Dataset

We will take the same CSV file as tho one used for the CVS plugin:

```csv {filename="sample_data.csv"}
timestamp,value,base_path,file_name
2024-05-15 14:30:45.123,42,"/home/user/documents","report.pdf"
2024-05-16 09:15:22.456,87,"C:\ProgramData\logs","application.log"
```

this file can be parsed with the following regular expression, as long as we *skip* the first line
```regex
^(?P<timestamp>[^,]*),(?P<value>\d*),"?(?P<base_path>[^,""\\]*)"?,"?(?P<base_pathss>[^,""\\]*)"?$
```
The name of the capture groups (eg: `timestamp`, `value`, etc.)  are used for the field mapping.

{{< callout type="warning" >}}
while this file can be parsed using a regular expression, we strongly recommend to use the CSV parser
{{< /callout >}}

## XML Descriptor

```xml {filename="configuration/regexp_plugin.xml"}
<?xml version="1.0" encoding="UTF-8"?>
<plugin parser="Regexp" file_encoding="UTF_8">
  <mapping data_type="win_reg_data">
    <description>
      <![CDATA[
Parses CSV file containing timestamped entries 
with numeric values, paths, and filenames.

- Timestamp records when each entry was logged.
- Value stores a numeric counter.
- Path and filename together identify file locations on the system.
]]>
    </description>
    <category>User Defined</category>
    <default_parser value="Ignore" />
    <default_date_pattern value='%Y-%m-%d %H:%M:%S.%3f' />
   
    <!-- The CSV header is on line 1 → skip it -->
    <skip_lines value="1" />

    <!-- an error is reported if a line fail to match the regexp -->
    <regexp_fail_policy value="Fail" />
    <regex>
    <![CDATA[^(?P<timestamp>[^,]*),(?P<value>\d*),"?(?P<base_path>[^,""\\]*)"?,"?(?P<base_pathss>[^,""\\]*)"?$]]>
    </regex>
   
    <timeline>
      <timeline_type value="Standard" />
      <description>
        <output_name value="full_path" />
      </description>
      <additional_description>
        <output_name value="count" />
      </additional_description>
    </timeline>

    <!-- Field mappings -->
    <fields>
      <field input="timestamp" output="timestamp" parser="DateTime"
        description="Timestamp of the event" />
      
      <field input="value" output="count" parser="Int"
        description="Numeric value associated with the entry" />
      
      <field input="base_path" output="directory" parser="String"
        description="Base directory path" />
      
      <field input="file_name" output="filename" parser="String"
        description="Name of the file" />
      
      <multi_input
          output="full_path"
          parser="Join"
          separator="/"
          avoid_separator_duplication="true"
          description="Full path combining directory and filename"
      >
        <field input="base_path" parser="String" />
        <field input="file_name" parser="String" />
      </multi_input>
    </fields>
  </mapping>
</plugin>
```
Key points:
- `<plugin parser="Regexp" >`: the plugin uses the `Regexp`python parser.
- `<skip_lines value="1" />`: the first line of the file is skipped to avoid parsing the csv header
- `<regexp_fail_policy value="Fail" />`: defines the policy to applys when a line fail to match the regular expression:
  - `Fail`: an error is reported for the line
  - `Skip`: the line is ignored
  - `Merge`: the line is merged with the content of the last field of the previous line. This is usefull for parsing log files that contains multiline records.
  - `<regex>`: the regular expression to use. it is *protected* from the XML interpreter using `<![CDATA[]>`

You can test the plugin with the following command
```bash
dfir-ogre plugin \
    --filename sample_data.csv \
    --plugin_config configuration/regexp_plugin.xml \
    --computer_name SAMPLE_HOST \
    --output_folder output
    --timeline 
```
