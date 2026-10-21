---
date: '2026-01-06T15:52:05+01:00'
lastmod: '2026-10-21'
title: 'Command line usage'
weight: 1
---

## Overview

Use the `dfir-ogre` command after installing and activating your environment.
Choose the command that matches your source data:

| Command | Use it to |
|---------|-----------|
| [`orc`](#the-orc-command) | Extract and parse DFIR-ORC archives using YAML mapping rules. |
| [`folder`](#the-folder-command) | Parse files collected from one computer, including unpacked ORC collections. |
| [`plugin`](#the-plugin-command) | Run one parser against one file, with output options supplied on the command line. |
| [`timeline`](#the-timeline-command) | Parse ORC archives and combine timeline records into a sorted CSV file. |
| [`list`](#the-list-command) | List available parsers using the libraries selected in a YAML configuration. |

Get help for the command or an individual subcommand:

```bash
dfir-ogre --help
dfir-ogre plugin --help
```

Examples below assume you are in the directory containing the sibling
`dfir-ogre/` and `dfir-ogre-plugin-windows/` checkouts. Adjust input paths and
configuration settings for your collection. Paths inside a YAML configuration
are resolved relative to your working directory.

The `orc`, `folder`, and `timeline` commands read their mappings and output
settings from a [YAML configuration](/usage/ogre_configuration/). The `plugin`
command takes an XML plugin descriptor directly and does not need a YAML file.
Use `dfir-ogre plugin` for individual parsers; the standalone `dfir-ogre-plugin`
command has been removed.

## The `orc` command

Parse archives belonging to one computer. The configuration selects files,
parsers, output formats, destinations, and the report directory.

| Parameter | Meaning |
|-----------|---------|
| `--archive` | **Required.** A `.7z` archive, comma-separated archive paths, an ORC `Outcome.json` path, or an inline JSON archive definition. |
| `--configuration` | **Required.** Path to the YAML configuration. |
| `--case` | Case name used when resolving the configuration. Default: `default_case`. |
| `--password` | Optional password for the outer archives. Passwords for nested archives are configured with `inner_archive_password` in YAML. |

### Parse an ORC outcome

```bash
dfir-ogre orc \
    --archive evidence/ORC_WorkStation_HOST01_Outcome.json \
    --configuration dfir-ogre/configuration/ogre.yaml \
    --case incident_001
```

Archive paths in an outcome file are resolved relative to that file. OGRE
extracts selected artifacts, applies the configured mappings, writes the
outputs, and creates a JSON processing report in `report_folder`. Check that
report for extraction and parsing errors.

### Parse several archives from one computer

```bash
dfir-ogre orc \
    --archive 'evidence/host1_general.7z,evidence/host1_details.7z' \
    --configuration dfir-ogre/configuration/ogre.yaml \
    --case incident_001
```

The archives are treated as one collection. When an ORC hostname cannot be
inferred from the first archive's name, its filename stem is used.

### Supply archive metadata as JSON

```bash
dfir-ogre orc \
    --archive '{"id":"collection-001","hostname":"HOST01","timestamp":"20261021_120000","unencrypted_data_files":["evidence/general.7z","evidence/details.7z"]}' \
    --configuration dfir-ogre/configuration/ogre.yaml \
    --case incident_001
```

The JSON object requires `id`, `hostname`, `timestamp`, and a nonempty
`unencrypted_data_files` array. `timestamp` uses `YYYYMMDD_HHMMSS` and is
interpreted as UTC. Optional `dir_tree` supplies a directory-tree value for
configuration placeholders. Archive paths in an inline definition are relative
to the working directory.

## The `folder` Command

Parse ordinary files from one computer without unpacking an archive. This also
supports collections that have already been extracted from DFIR-ORC.

| Parameter | Meaning |
|-----------|---------|
| `--folder` | **Required.** Root directory containing the source artifacts. Subdirectories are scanned. |
| `--configuration` | **Required.** Path to the YAML configuration containing mappings and output definitions. |
| `--computer_name` | Computer name stored in metadata. Defaults to the source directory's name. |
| `--case` | Case name used when resolving the configuration. Default: `default_case`. |

```bash
dfir-ogre folder \
    --folder evidence/HOST01 \
    --configuration dfir-ogre/configuration/ogre.yaml \
    --computer_name HOST01 \
    --case incident_001
```

Files are read in place. `archive_file_pattern` rules match paths relative to
the source root. `original_file_pattern` rules use original Windows paths from
`GetThis.csv` files discovered throughout the collection; they do not infer
original paths from the physical folder layout. Files without a matching index
entry can still be selected by `archive_file_pattern` rules.

Use `$relative_path` in YAML output definitions to preserve source directory
context. In `output_folder` it retains directories; in `base_file_name` it is
flattened into a filename. See [configuration placeholders](/usage/ogre_configuration/#placeholder-variables).

Folder processing writes a JSON report containing the source folder and run ID.
Extraction/preparation or parsing errors produce a nonzero exit status.

## The `plugin` Command

Run one parser against one existing file. The XML descriptor selects the parser
and its data-type mappings. This is useful for individual artifacts and for
checking a parser without preparing an archive or folder configuration.

| Parameter | Meaning |
|-----------|---------|
| `--filename` | **Required.** Path to the input file. |
| `--plugin_config` | **Required.** Path to the XML plugin descriptor. |
| `--computer_name` | **Required.** Computer identifier stored in output metadata. |
| `--output_folder` | **Required.** Destination directory; created during parsing if necessary. |
| `--output_type` | `file` (default) or `gzip`. |
| `--output_format` | `jsonl` (default), `csv`, `normalized_jsonl`, `normalized_csv`, or `analytics_jsonl`. See [output formats](/usage/artefacts_format/). |
| `--compression_level` | Gzip compression level, 0–9; default: 5. Requires `--output_type gzip`. Level 0 retains gzip framing without compression. |
| `--output_name` | Base filename template. Default: `$file_name`. See [filename templates](#filename-templates). |
| `--output_date_format` | `iso` (default), `iso_utc`, `utc_naive`, or a custom chrono strftime pattern, such as `'%Y-%m-%d %H:%M:%S'`. |
| `--params` | JSON object containing parser-specific parameters. Values are converted to strings before being passed to the parser. |
| `--timeline` | Emit timeline entries using the XML timeline configuration. Off by default. |
| `--timeline_include_undated` | Retain entries without dates as null-timestamp timeline entries. Requires `--timeline`; incompatible with `analytics_jsonl`. |
| `--include_empty` | Include null fields in the output. Off by default. |
| `--timeout` | Maximum worker runtime in seconds. Default: 60. |
| `--library` | Additional Python library to import for [custom parsers](/plugin-creation/custom_library/). The library must be installed or importable in the active environment. |
| `--dry_run` | Validate settings and print a JSON plan without parsing the artifact or creating output files. |

### Parse an individual artifact

```bash
dfir-ogre plugin \
    --filename evidence/application.pf \
    --plugin_config dfir-ogre-plugin-windows/configuration/prefetch.xml \
    --computer_name HOST01 \
    --output_folder output/prefetch
```

With the default naming and format, this produces
`output/prefetch/application.prefetch.jsonl`.

### Filename templates

The template controls the base filename. OGRE appends the XML data type and the
format/compression extension automatically. Each data type stays in its own file,
which is useful for artifacts such as SRUM that contain several providers.

| Placeholder | Meaning |
|-------------|---------|
| `$file_name` | Input filename without its final extension; `SRUDB.dat` becomes `SRUDB`. |
| `$computer_name` | Value supplied through `--computer_name`. |
| `$parser` | Parser command from the XML descriptor, such as `Srum`. |
| `$timestamp` | One invocation timestamp in UTC, formatted as `YYYYMMDD_HHMMSS`. |

Braced placeholders such as `${file_name}` are also accepted. Use `$$` for a
literal dollar sign. Quote templates with single quotes so your shell does not
expand them. Unknown placeholders, empty names, path separators, and invalid
filename characters cause an error. Use `--output_folder` to choose a directory.

```bash
dfir-ogre plugin \
    --filename evidence/SRUDB.dat \
    --plugin_config dfir-ogre-plugin-windows/configuration/srum.xml \
    --computer_name HOST01 \
    --output_folder output/srum \
    --output_type gzip \
    --compression_level 5 \
    --output_name '${computer_name}_${parser}_${file_name}_${timestamp}'
```

One resulting filename could be
`HOST01_Srum_SRUDB_20261021_120000.srum_application_resources.jsonl.gz`.

### Preview a run

Add `--dry_run` to inspect the parser, resolved base name, output settings, and
possible files:

```bash
dfir-ogre plugin \
    --filename evidence/SRUDB.dat \
    --plugin_config dfir-ogre-plugin-windows/configuration/srum.xml \
    --computer_name HOST01 \
    --output_folder output/srum \
    --output_type gzip \
    --output_format normalized_jsonl \
    --timeline \
    --dry_run
```

The JSON plan includes `parser`, `input_file`, `output_folder`, `base_file_name`,
`output_type`, `format`, `date_format`, timeline options, and a `files` array.
It lists possible files from every XML mapping. A real run may produce only a
subset when the artifact lacks some data types. Dry-run checks that the input
file exists, but does not read its contents or execute the parser's mapping
logic. The computer name is supplied by the caller; no host identification is
performed on the artifact.

A later invocation expands `$timestamp` again, so a timestamped filename can
differ from the one shown in an earlier preview.

### Existing files and failures

The plugin command errors if a planned output target already exists. It neither
appends to nor overwrites existing files, including when another invocation
creates a target while parsing is in progress. This applies to data files and,
for normalized/analytics formats, shared metadata and timeline companion files.

For a base name of `SRUDB`, `normalized_jsonl` with gzip and timeline enabled can
produce:

```text
SRUDB.srum_application_resources.jsonl.gz
SRUDB.srum_application_resources.tl.jsonl.gz
ogre_metadata.jsonl.gz
```

Changing the base name can resolve a data-file collision. Shared metadata names
are fixed, so an existing `ogre_metadata` file requires a new output directory.
These existence checks also run in dry-run mode.

Parser errors, output errors, unknown parsers, crashes, and timeouts return a
nonzero exit status. A parser can report errors while still producing valid
records; those partial results remain available. Check the errors before using
them as a complete extraction.

## The `timeline` Command

Parse ORC archives and create one CSV sorted by timestamp. Use the supplied
`ogre_timeline.yaml`, which configures the intermediate timeline files expected
by this command.

| Parameter | Meaning |
|-----------|---------|
| `--archive` | **Required.** Archive input in the same forms accepted by `orc`. |
| `--configuration` | **Required.** Path to the timeline YAML configuration. |
| `--timeline_folder` | **Required.** Destination for `<computer>.timeline.csv`. |
| `--case` | Case name used when resolving the configuration. Default: `default_case`. |
| `--password` | Optional password for the outer archives. |

```bash
dfir-ogre timeline \
    --archive evidence/ORC_WorkStation_HOST01_Outcome.json \
    --configuration dfir-ogre/configuration/ogre_timeline.yaml \
    --timeline_folder output/timeline \
    --case incident_001
```

The final CSV remains in `--timeline_folder`. The intermediate directories
specified by this command's `temp_folder` and `output_folder` configuration are
removed after timeline generation; use dedicated locations for those settings.

## The `list` Command

List parser names and descriptions from the Python libraries selected by
`plugin_prefixes` in the YAML configuration.

| Parameter | Meaning |
|-----------|---------|
| `--configuration` | **Required.** Path to the YAML configuration. |
| `--case` | Case name used when resolving the configuration. Default: `default_case`. |

```bash
dfir-ogre list \
    --configuration dfir-ogre/configuration/ogre.yaml \
    --case incident_001
```

The output is a table of parser commands and descriptions. Use the matching XML
descriptor when running a parser with `dfir-ogre plugin`.
