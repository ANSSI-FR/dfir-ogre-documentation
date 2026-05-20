---
date: '2026-01-06T15:52:05+01:00'
title: 'Command line usage'
weight: 1
---

## Overview

The command line has three main usages:

**`orc`**: Unpacks DFIR-ORC archives and runs every parser defined in the YAML configuration on the extracted files.  

Typical usage:  
```bash
dfir-ogre orc \
    --archive myarchive.7z
    --configuration ogre.yaml
    [--case <name>]
```  
{{< callout >}}
The `ogre.yaml` [configuration file](/usage/ogre_configuration/ "Ogre configuration") tells the CLI which parsers (plugins) to run, where to read source files,  where to write outputs, and how the generated artefacts should be formatted. 

A ready to use ogre.yaml file is provided in the `dfir-ogre/configuration/` folder.
{{</ callout >}}

---
**`timeline`**: Same as `orc` but creates a single CSV file that contains a sorted timeline.

It requires a specific `ogre.yaml` file provided here `dfir-ogre/configuration/ogre_timeline.yaml` .

```bash
dfir-ogre timeline \
    --archive secret.7z \
    --timeline_folder ./timeline \
    --configuration ogre_timeline.yaml
```  


---
**`plugin`**: Executes a single plugin on a single input file. Useful for debugging or ad‑hoc analysis without dealing with archives.  
Typical usage:  
```bash
dfir-ogre plugin \
    --filename sample.txt \
    --plugin_config sample_plugin.xml \
    --computer_name HOST01 \
    --output_folder ./out \
```  


---

##  The `orc` command

Unpacks DFIR-ORC archives and runs every parser defined in the YAML configuration on the extracted files.

### Parameters

| Parameter | Description |
|-----------|-------------|
| `--archive` | **Required**. Can be one of four forms: <br>• A **single** 7z/zip archive file path. <br>• A **comma‑separated list** of archive files (treated as one case). <br>• A path to an Orc `xxx_Outcome.json` file.<br>• A **JSON string** that describes the archives to be parsed  |
| `--configuration` | path to the `ogre.yaml` configuration|
| `--case` | Overrides the case name coming from the configuration or the ORC metadata. |


### What happens internally

1. **Extraction**: each archive is extracted into `temp_folder`  
2. **File matching**: for every entry in the `mapping` section of the configuration, the CLI evaluates the appropriate regex (`original_file_pattern` *or* `archive_file_pattern`). 
3. **Parser execution**: matching files are handed to the configured parser plugin. 
4. **Output generation**: according to the `output:` definitions (rawjson, gzip, timeline, …) the parsed records are stored in the paths built from placeholders (`$output_folder`, `$archive_name`, `$mapping_label`, …).
5. **Reporting**: a JSON report summarising success/failure per parser is created. 


### Example (ORC outcome)

```bash
dfir-ogre orc \
    --archive ORC_xxx_Outcome.json \
    --configuration configuration/ogre.yaml
```

Every archives defined in the outcome will be processed, and some metadata will be included in the parsed records

### Example (multiple archives)

```bash
dfir-ogre orc \
    --archive "host1.7z,host1_small.7z,host1_detailled.7z" \
    --configuration configuration/ogre.yaml
```

All three archives are processed as a single **DFIR-ORC** from a single machine whose name defaults to the first archive (`host1`).

### Example (json_ data)

```bash
dfir-ogre orc \
    --archive '{"id": "the_host_id","hostname": "HOSTNAME", "unencrypted_data_files":["file1.7z","file2.7z"]'} \
    --configuration ogre.yaml
```

The JSON must contain at least:

```json
{
  "id": "the_host_id",
  "hostname": "HOSTNAME",
  "timestamp": "20250904_221144",
  "unencrypted_data_files": ["file1.7z","file2.7z"]
}
```

Optional field:
* `dir_tree` – a relative path that can be appended to every output folder (useful for hierarchical storage).  



## The `timeline` Command

The `timeline` sub‑command is a thin wrapper around the `orc` command that creates a single CSV file that contains a sorted timeline.

It requires a specific `ogre_timeline.yaml` configuration file that can be found in the in the `/dfir-ogre/configuration/` folder

```bash
dfir-ogre timeline \
    --archive ORC_xxx_Outcome.json \
    --timeline_folder ./timeline_output/ \
    --configuration configuration/ogre_timeline.yaml
```

The generated timeline is placed in the directory you provide via `--timeline_folder`.

## The `plugin` Command
Run a plugin against a single file. Typical use‑case:
 - parse data that is not located in an orc archive.
 - debug a single plugin without the overhead of unpacking an entire ORC archive.

| Parameter | Meaning |
|-----------|---------|
| `--filename` | The file that the parser will receive. |
| `--plugin_config` | Path to the plugin’s XML configuration. |
| `--computer_name` | computer identifier that will be stored in the metadata. |
| `--output_folder` | Destination directory for the parser’s output. |
| `--output_format` | the [output format](/usage/artefacts_format/). defaults to `jsonl` |
| `--output_date_format` | the output date format (`iso`, `iso_utc` or `naive_utc`). defaults to `iso_utc` |
| `--params` | JSON object passed verbatim to the parser (some plugins need extra parameters). |
| `--timeline` | If present, the parser is asked to emit timeline entries. |
| `--include_empty` | Keep empty fields in the final JSON output. |
| `--library` | optional, reference a [custom plugin library](/plugin-creation/custom_library/)  |


*Example*

```bash
dfir-ogre plugin \
    --filename sample.txt \
    --plugin_config plugins/sample_text.xml \
    --computer_name WORKSTATION01 \
    --output_folder ./tmp/plugin_out \
    --params '{"ignore_header":true}'
```

## The `list` Command

List every python parsers that can be used by an `ogre.yaml` configuration file

*Usage*

```bash
dfir-ogre list --configuration ogre.yaml
```

*What it does*  
- Loads every Python package whose name begins with one of the `plugin_prefixes` declared in the configuration.  
- Instantiates each discovered parser and prints its name and description.

Output (truncated)

```
┌───────────┬───────────────────────────────────────┐
│ Command   │ Description                           │
├───────────┼───────────────────────────────────────┤
│ Csv       │ Generic CSV parser                    │
│ Evtx      │ Windows Event Log parser              │
│ NTFSInfo  │ NTFSInfo parser                       │
│ Void      │ No‑op parser – useful for testing     │
└───────────┴───────────────────────────────────────┘
```
