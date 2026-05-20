---
date: '2026-01-06T15:52:05+01:00'
title: 'Configuration guide'
weight: 2
---

Most of **DFIR-OGRE** commands relies on a `ogre.yaml` configuration file, It tells the CLI where to write outputs, how the generated records should be formatted and which plugins to run on which file.

{{< callout type="important" >}}Ready to use `ogre.yaml` files are provided in the `dfir-ogre/configuration/` folder.
{{< /callout >}}

{{< callout type="important" >}}The configuration files for the default plugins are available in the `dfir-ogre-plugin-windows/configuration/` folder.
{{< /callout >}}

## Overview

Here is a example of a configuration file.

```yaml
plugin_prefixes:
    - dfir_ogre_plugin

case: a_victim
output_folder: output/$case/
report_folder: output/$case/report
temp_folder: tmp_ogre
inner_archive_password: avproof
plugin_folder: dfir-ogre-plugin-windows/configuration/ 

output:
    timeline:
        type: gzip
        format: jsonl
        date_format: iso_utc
        with_timeline: true
        include_empty_field: false
        output_folder: $output_folder/timeline/$mapping_label/$computer_name
        base_file_name: $file_name
    
    raw_data:
        type: file
        format: jsonl
        date_format: iso_utc
        with_timeline: true
        include_empty_field: false
        output_folder: $output_folder/raw/$mapping_label/$computer_name
        base_file_name: $file_name

mapping:
    # ActivityCache
    - original_file_pattern: '.*\\ActivitiesCache.db$'
      plugin_file: $plugin_folder/activity_cache.xml
      mapping_label: activity_cache
      output:
          - timeline
          - raw_data
          
    # NTFSInfo
    - archive_file_pattern: 'NTFSInfo.*\.csv$'
    plugin_file: $plugin_folder/ntfs_info.xml
    mapping_label: ntfs_info
    output:
        - timeline

```

## General Settings

- **plugin_prefixes** : A comma separated list of Python package name prefixes that will be loaded to discover available parsers.  
- **case** : name of the case.  
- **output_folder** : Base directory where all generated artefacts are stored.
- **temp_folder** : Temporary directory used while processing an ORC archive (e.g., to unpack files)  
- **report_folder** : at the end of each DFIR-OGRE execution, a summary report of the extraction process is generated and placed in the configured directory.
- **plugin_folder** : Base directory where all **XML plugin descriptors** are found. Plugins are described using xml files. Default plugins filed are available in the `dfir-ogre-plugin-windows/configuration/` folder
- **inner_archive_password** : Default password used for encrypted inner archives.  


## Place‑holder Variables

The configuration file uses a few **runtime placeholders** that are substituted during the parsing:

| Placeholder | What it expands to |
|-------------|--------------------|
| `$output_folder` | The global `output_folder` defined at the top of the file (with `$case` already replaced). |
| `$plugin_folder` | The global 'plugin_folder' defined at the top of the file |
| `$case` | The global 'case' name defined at the top of the file |
| `$computer_name` | The computer name extracted from the ORC metadata. |
| `$mapping_label` | The `mapping_label` of the *current* mapping entry. |
| `$file_name` | Base name of the extracted source file (without extension). |
| `$dir_tree` | Directory tree defined when using the CLI whith json parameters |

## Output Section: how to write extracted artefacts

The `output` block defines output "templates", 
each entry can be referenced in the `mapping` section via the `output:` parameter.

### Example
```yaml
timeline:
    type: gzip
    format: jsonl
    date_format: iso_utc
    with_timeline: true
    include_empty_field: false
    output_folder: $output_folder/timeline_data/$mapping_label/$computer_name
    base_file_name: $file_name
```

This example defines an output template named `timeline` that will write JSONL timeline data in compressed files. 

### Parameters

- **type**: The output type. Currently only two exist:
  - *file*: writes the data to a file.
  - *gzip*: compresses the data into a gzip file.

- **format**: Defines the output data format:
  - *json*: data is written in JSONL format.
  - *csv*: The is are written in the CSV format.
  - *normalized_json*: data is extracted in a normalized JSONL format that avoids data duplication (see [output format](/usage/artefacts_format/#normalized-formats).
  - *normalized_csv*: data is extracted in a normalized JSONL format that avoids data duplication (see [output format](/usage/artefacts_format/#normalized-formats).


- **date_format**: The output date format. The following formats are supported:
  - *iso*: ISO‑8601 format with timezone information. Example: *1978-04-16T10:31:42.123456+02:00*.
  - *iso_utc*: ISO‑8601 format converted to UTC with timezone information. Example: *1978-04-16T08:31:42.123456+00:00*.
  - *utc_naive*: Simple UTC format without timezone (some downstream systems may prefer this incomplete format). Example: *1978-04-16 08:31:42.123456*.

- **with_timeline**: Indicates whether a timeline format should be included. During parsing, an error will be raised if the plugin does not support timeline generation.

- **include_empty_field**: Indicates whether empty fields should be included in the output.

- **output_folder**: The output directory; note in the example that the path is be generated dynamically using placeholder variables.

- **base_file_name**: The output file name; note in the example using placeholder variables.

- **compression_level**: (Optional, between 1 and 9) Specifies the desired compression level for gzip output. Level 1 provides the lowest compression (and fastest speed). Default value: 5.


## Mapping Section: Which plugin processes which artefact?

The `mapping` list is the heart the data extraction. Each entry tells Ogre:

* **Which files to match**:
    *  `original_file_pattern`: a regular expression that will be match against file names found in the `GetThis.csv` files.
    *  `archive_file_pattern`: a regular expression that will be matched against file name found in the archive.
* **Which XML plugin descriptor** to load (`plugin_file`).  
* **What label** to give the output (`mapping_label`): this label is a **runtime placeholders** that can be used in the output configuration
* **Which output template** to use (`output:` list of outputs that will consume the artefact).  


### Example

```yaml

- original_file_pattern: '.*\\ActivitiesCache.db$'
  plugin_file: $plugin_folder/activity_cache.xml
  mapping_label: activity_cache
  output:
      - timeline
```

This example tells DFIR_OGRE:
1. to search for the `ActivitiesCache.db` original file name
2. launch the plugin defined in `activity_cache.xml`
3. write result using the `timeline` output template
