---
date: '2026-01-06T15:54:09+01:00'
title: 'Sqlite plugin'
cascade:
  type: docs
  params:
    breadcrumbs: true
weight: 3
---

A guides to create a plugin that parses the result of a SQL query performed on a SQLite database.

It is not as detailled that the [CSV tutorial](/plugin-creation/generic_plugins/csv_tutorial/) and focus on the specific features

{{< callout type="warning" >}}
No sample data is provided for this example
{{< /callout >}}

## XML Descriptor

```xml {filename="configuration/sqlite_plugin.xml"}
<?xml version="1.0" encoding="UTF-8"?>
<plugin parser="SQLite" >
  <mapping data_type="win_sql_data">
    <default_parser value="Ignore" />
    <default_date_pattern value='timestamp' />
   
    <!-- sqlite specific parameters -->
    <query>
    <![CDATA[ 
      SELECT timestamp,value,base_path,file_name 
      FROM sample_table 
      ORDER BY timestamp
      ]]>
    </query>
   
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
- `<plugin parser="SQLite" >`: the plugin uses the `SQLite`python parser.
- `<query>` : the SQL query to perform

You can test the plugin with the following command. 
```bash
dfir-ogre plugin \
    --filename my_sqlite_database.db \
    --plugin_config configuration/sqlite_plugin.xml \
    --computer_name SAMPLE_HOST \
    --output_folder output
    --timeline 
```
