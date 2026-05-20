---
date: '2026-01-06T15:54:09+01:00'
title: 'CSV plugin tutorial'
cascade:
  type: docs
  params:
    breadcrumbs: true
weight: 1
---

This tutorial guides you through creating an plugin that parses a CSV file

## Sample Dataset

Before starting, let's create our sample CSV file :

```csv {filename="sample_data.csv"}
timestamp,value,base_path,file_name
2024-05-15 14:30:45.123,42,"/home/user/documents","report.pdf"
2024-05-16 09:15:22.456,87,"C:\ProgramData\logs","application.log"
```

The structure is:
| Column | Description |
|--------|-------------|
| `timestamp` | Date/time value (format: `YYYY-MM-DD HH:MM:SS.sss`) |
| `value` | A numeric value |
| `base_path` | Directory path |
| `file_name` | File name only |

Save this as `sample_data.csv` for testing.

---

{{% steps %}}

## Create the XML Descriptor Template

Create a new file named `csv_plugin.xml` in your configuration directory:

```xml {filename="configuration/csv_plugin.xml"}
<?xml version="1.0" encoding="UTF-8"?>
<plugin parser="Csv" file_encoding="UTF_8">
  <mapping data_type="win_custom_data">
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
  
    <csv_delimiter value="," />
    <default_parser value="String" />
    
    <fields>
      <!-- Fields will be defined in Step 2 -->
    </fields>
  </mapping>
</plugin>
```

Key points:
- `parser="Csv"` tells DFIR-OGRE to use the CSV python parser
- `data_type="win_custom_data"` is an identifier for the artefacts that will be extracted by this plugin.
- `file_encoding="UTF_8"` specifies the encoding of the input file 
- `csv_delimiter` specifies the CSV column delimiter
- `<default_parser value="String">` columns that are not defined in the `<fields>` section will be treated as String. The other possible value is "Ignore" (the column is not parsed). See next step for the `<fields>` definition

The `<description>` and `<category>` are for documentation purpose.

This descriptor can be tested with the command:
```bash
dfir-ogre plugin \
    --filename sample_data.csv \
    --plugin_config configuration/custom_csv.xml \
    --computer_name SAMPLE_HOST \
    --output_folder output
```
This command should create a file `csv_tuto.win_custom_data.jsonl` with two json lines.

{{< callout >}}
You will notice that every field is parsed as a string. The next step will show you how to properly parse each field.
{{< /callout >}}


---

## Define Field Mappings

Now let's map each CSV columns. For each column in the csv file we add a `<field >` that defines its:
- `input`: the column name
- `output` (optional): the name in the json file
- `parser`: whether it will be parsed as a DateTime, an Int, a String, etc.

```xml {filename="configuration/csv_plugin.xml"}
<plugin parser="Csv" file_encoding="UTF_8">
  <mapping data_type="win_custom_data">
    <!-- ... previous sections ... -->
    <csv_delimiter value="," />
    <default_parser value="Ignore" />
    <default_date_pattern value="%Y-%m-%d %H:%M:%S.%3f"/>
    
    <fields>
      <field input="timestamp" parser="DateTime"
        description="Timestamp of the event" />
      
      <field input="value" output="count" parser="Int"
        description="Numeric value associated with the entry" />
      
      <field input="base_path" output="directory" parser="String"
        description="Base directory path" />
      
      <field input="file_name" output="filename" parser="String"
        description="Name of the file" />
    </fields>
  </mapping>
</plugin>
```

Key points:
- `default_date_pattern value="%Y-%m-%d %H:%M:%S.%3f"`: fields that have a `DateTime` parser will be parsed with this pattern.
- `default_parser value="Ignore"`: columns that are not in the field mappping are ignored 

if you run the `dfir-ogre` command again, the `csv_tuto.win_custom_data.jsonl` now contains:
- the `timestamp` field is now in iso format (ie: "2024-05-15T14:30:45.123000+00:00")
- the previous `value` field has been renamed to count and contains integer values
- the `base_path` and `file_name` have been renamed to `directory` and `filename`

{{< callout type="warning" >}}
The plugins write data in *append* mode. If you don't delete `csv_tuto.win_custom_data.jsonl` before running the command, two new lines will be added at the end of the file.
{{< /callout >}}

Now that we have a plugin that properly parse dates, the next step will describe how to use the `timeline` format

---

## Add Timeline Configuration

To enable `timeline` format, add a `<timeline>` section. When called with the proper arguments, the plugin will generate one line per `DateTime` field and add description fields that describes the most important data for the artiefact.

```xml {filename="csv_plugin.xml"}
<?xml version="1.0" encoding="UTF-8"?>
<plugin parser="Csv" file_encoding="UTF_8">
  <mapping data_type="win_custom_data">
    <!-- ... previous sections ... -->

    <!-- Timeline definition -->
    <timeline>
      <timeline_type value="Standard" />
      <description>
        <output_name value="filename" />
      </description>
      <additional_description>
        <output_name value="directory" />
        <output_name value="count" />
      </additional_description>
    </timeline>

    <fields>
      <!-- ... field mappings ... -->
    </fields>
  </mapping>
</plugin>
```

Timeline elements:
- `<timeline_type>`: Use "Standard" for regular timestamp events
- `<description>`: show the most important fields (filename). 
- `<additional_description>`: Additional context data

You can now generate timeline output with the command:
```bash
dfir-ogre plugin \
    --filename sample_data.csv \
    --plugin_config configuration/csv_plugin.xml \
    --computer_name SAMPLE_HOST \
    --output_folder output
    --timeline 
```

The output `csv_tuto.win_custom_data.jsonl` should now contains timeline formated json line like this one (expanded in several line for lisibility)
```json
{
    "timestamp":"2024-05-15T14:30:45.123000+00:00",
    "timestamp_meaning":"timestamp",
    "data_type":"win_custom_data",
    "related_user":"",
    "description":"filename: report.pdf",
    "additional_description":"count: 42 - directory: /home/user/documents",
    "metadata":{
        "computer":"SAMPLE_HOST",
        "data_type":"win_custom_data_2",
        "archive_filename":"tuto/csv_tuto.txt"
    },
    "data":{
        "timestamp":"2024-05-15T14:30:45.123000+00:00",
        "count":42,
        "directory":"/home/user/documents",
        "filename":"report.pdf"
    }
}
```

---

## (Optional): Merge Path and Filename

It is possible to combine several fields together using a `<multi_input>` mapping. The following configuration combines `base_path` and `file_name` into a single `full_path` field:

```xml {filename="custom_csv.xml"}
<?xml version="1.0" encoding="UTF-8"?>
<plugin parser="Csv" file_encoding="UTF_8">
  <mapping data_type="win_custom_data">
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
    <csv_delimiter value="," />

    <!-- Timeline definition -->
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
      
      <!-- Multi-input to join path components -->
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

The `<multi_input>` configuration:
- Uses `parser="Join"` to concatenate strings
- `separator="/"` sets the path separator (use `\\` for Windows paths)
- `avoid_separator_duplication="true"` prevents double separators if they exist

It is not mandatory to  keep the two `base_path` and `file_name` `<field>` definition, you can remove them from <fields>.

{{% /steps %}}

{{< callout >}}
That's it, you now have all the basis to create Csv plugins, 
you can refer to the [XML Descriptor documentation](/plugin-creation/xml_descriptor/) for additional details and configuration options.
{{< /callout >}}
