---
date: '2026-01-06T15:52:05+01:00'
lastmod: '2026-10-21'
title: 'Configuration guide'
weight: 2
---

The `orc`, `folder`, `timeline`, and `list` commands use an `ogre.yaml`
configuration file. It selects plugin libraries, maps source files to parsers,
and defines output destinations and formats. The single-file `plugin` command
takes those output settings directly on the command line.

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

# Optionnal log configuration
# log_file_path: ./
# log_file_name: dfir-ogre.log
# log_level: INFO # ERROR DEBUG
# log_max_bytes: 5242880 #1024*1024*5 (5Mb)
# log_backup_count: 3

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
        with_timeline: false
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

- **plugin_prefixes**: A YAML list of Python package name prefixes used to discover available parsers.
- **case** : name of the case.  
- **output_folder** : Base directory where all generated artefacts are stored.
- **temp_folder** : Temporary directory used while processing an ORC archive (e.g., to unpack files)  
- **report_folder** : at the end of each DFIR-OGRE execution, a summary report of the extraction process is generated and placed in the configured directory.
- **plugin_folder** : Base directory where all **XML plugin descriptors** are found. Plugins are described using xml files. Default plugins filed are available in the `dfir-ogre-plugin-windows/configuration/` folder
- **inner_archive_password** : Default password used for encrypted inner archives.  


## Placeholder Variables

The configuration file uses a few **runtime placeholders** that are substituted during the parsing:

| Placeholder | What it expands to |
|-------------|--------------------|
| `$output_folder` | The global `output_folder` defined at the top of the file (with `$case` already replaced). |
| `$plugin_folder` | The global 'plugin_folder' defined at the top of the file |
| `$case` | The global 'case' name defined at the top of the file |
| `$computer_name` | Computer name from ORC metadata, or the name selected for a `folder` run. |
| `$mapping_label` | The `mapping_label` of the *current* mapping entry. |
| `$file_name` | Base name of the extracted source file (without extension). |
| `$parser` | Parser command from the XML descriptor. |
| `$timestamp` | Collection timestamp in `YYYYMMDD_HHMMSS` form; folder runs use the invocation time. |
| `$archive_name` | Source archive's filename stem; folder runs use the source folder's name. |
| `$relative_path` | Source parent path. Preserves directories in `output_folder`; flattens separators to underscores in `base_file_name`. |
| `$dir_tree` | Directory tree defined when using the CLI whith json parameters |

These variables belong to YAML configuration resolution. For the four variables
available to the single-file CLI, see [plugin filename templates](/usage/command_line_usage/#filename-templates).

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
    timeline_include_undated: true
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
  - `jsonl`: JSON Lines, with metadata embedded in each record.
  - `csv`: semicolon-delimited CSV.
  - `normalized_jsonl`: data, metadata, and optional timeline records in separate JSONL files.
  - `normalized_csv`: data, metadata, and optional timeline records in separate CSV files.
  - `analytics_jsonl`: JSONL with an analytics envelope around each data record, plus separate metadata and optional timeline files.

  See [output formats](/usage/artefacts_format/) for the record layouts.


- **date_format**: The output date format. The following formats are supported:
  - `iso` or `iso_utc`: ISO-8601 in UTC with microseconds and an explicit offset. Both currently produce values such as `1978-04-16T08:31:42.123456+00:00`.
  - *utc_naive*: Simple UTC format without timezone (some downstream systems may prefer this incomplete format). Example: *1978-04-16 08:31:42.123456*.
  - A custom chrono strftime pattern, such as `'%Y-%m-%d %H:%M:%S'`.

- **with_timeline**: Request timeline entries using the XML descriptor's timeline
  configuration. Use a descriptor defining timeline rules to obtain those entries.

- **timeline_include_undated**: With `with_timeline: true`, emit a placeholder
  timeline entry when no valid date is available, using `timestamp: null` and
  `timestamp_meaning: "empty placeholder"`. Defaults to `false` and is incompatible
  with `analytics_jsonl`.

- **include_empty_field**: Indicates whether empty fields should be included in the output.

- **output_folder**: The output directory; note in the example that the path is be generated dynamically using placeholder variables.

- **base_file_name**: The output file name; note in the example using placeholder variables.

- **compression_level**: Optional gzip compression level from 0 to 9. Level 0
  disables compression while retaining gzip framing; level 1 favors speed and
  level 9 favors compression. Default: 5.


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


## Logging Configuration

### Overview

DFIR-OGRE supports two logging modes: **stdout-only** (default) and **file + stdout** (optional, configured via `ogre.yaml`).

Logs use this format:
```
YYYY-MM-DD HH:MM:SS,mmm - LEVEL - Message
```

### Default (No File Logging)

If no config file is provided, or the config file lacks log settings, dfir-ogre outputs to **stdout only** at `INFO` level. No log files are created.

### File Logging

To enable log rotation to a file, uncomment and set the `log_*` options in `configuration/ogre.yaml`:

```yaml {filename="configuration/ogre.yaml"}
log_file_name: dfir-ogre.log
log_file_path: ./
log_level: INFO
log_max_bytes: 5242880
log_backup_count: 3
```

| Option | Type | Default | Description |
|---|---|---|---|
| `log_file_name` | string | *(none)* | Log file name. **Required** — if omitted, file logging is disabled entirely. |
| `log_file_path` | string | `./` | Directory for the log file. Created automatically if missing. |
| `log_level` | string | `INFO` | Minimum level: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |
| `log_max_bytes` | int | `5242880` (5 MB) | Max size per log file before rotation. |
| `log_backup_count` | int | `3` | Number of rotated `.1`, `.2`, `.3` backup files to keep. |
