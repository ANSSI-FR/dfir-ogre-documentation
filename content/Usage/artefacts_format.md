---
date: '2026-01-06T15:52:05+01:00'
lastmod: '2026-10-21'
title: 'Artefact formats'
weight: 3
---

DFIR-OGRE provides several output formats for extracted artifacts. Select one
with `--output_format` for the [plugin command](/usage/command_line_usage/#the-plugin-command),
or `format` in a YAML output definition. Compression is selected separately with
`--output_type gzip` or `type: gzip` in YAML.

| Format | Layout |
|--------|--------|
| `jsonl` | JSON Lines with embedded metadata; `--timeline` selects timeline records. |
| `csv` | Semicolon-delimited CSV; `--timeline` selects timeline records. |
| `normalized_jsonl` | Separate JSONL data, metadata, and optional timeline files. |
| `normalized_csv` | Separate CSV data, metadata, and optional timeline files. |
| `analytics_jsonl` | JSONL data envelopes with computer and data-type fields, plus separate metadata and optional timeline files. |

## Raw format

For `jsonl` or `csv`, use `with_timeline: false` in YAML or omit `--timeline`
on the plugin command. Each parsed record contains the artifact fields and
embedded source metadata. In JSONL, the metadata field is named `ogre_md`.

**Example:**
  ```json
  {
      "ogre_md": {
        "archive": "ORC_Server_SRV-General.7z",
        "subarchive": "Event.7z",
        "computer": "SRV-HV01"
      },
      "system": {
        "time_created": {
          "system_time": "2021-04-14T21:30:24.000000Z"
        },
        "provider": {
          "provider_name": "Microsoft-Windows-Kernel-PnP"
        }
      },
      "event_data": {
        "device_instance_id":"ROOT\\ACPI_HAL\\0000",
        "driver_name":"hal.inf"
      }
  }
  ```


## Timeline format

For `jsonl` or `csv`, enable `with_timeline: true` in YAML or `--timeline`
on the plugin command. Timeline records include `timestamp`, its meaning,
summary fields, the original parsed `data`, and source `metadata`.

Dates with the same value within a parsed record can share one timeline entry
with combined timestamp meanings. For **NTFSInfo** and **USNInfo**, timestamp
meanings follow the MACB convention.

Use `--timeline_include_undated` (or its YAML equivalent) to retain a placeholder
entry when no valid date is available.

**Example:**
```json
{
    "timestamp": "2021-04-14T21:30:24.000000+00:00",
    "timestamp_meaning": "Event generation time",
    "data_type": "windows_events",
    "related_user": "S-1-5-18",
    "description": "Microsoft-Windows-Kernel-PnP:403",
    "additional_description": "device_instance_id: ROOT\\ACPI_HAL\\0000 - driver_name: hal.inf",
    "data": {
        "system": {
          "time_created": {
            "system_time": "2021-04-14T21:30:24.000000Z"
          },
          "provider": {
            "provider_name": "Microsoft-Windows-Kernel-PnP"
          }
        },
        "event_data": {
          "device_instance_id":"ROOT\\ACPI_HAL\\0000",
          "driver_name":"hal.inf"
        }
    },
    "metadata": {
        "archive": "ORC_Server_SRV-General.7z",
        "subarchive": "Event.7z",
        "computer": "SRV-HV01"
    }
}
```

## Normalized formats

Normalized formats separate artifact data, source metadata, and timeline records
into distinct files, linked by identifiers. This reduces repeated embedded
metadata and avoids repeating the artifact fields for every timeline timestamp.

Select `normalized_jsonl` or `normalized_csv`. Data records contain `ogre_id`
and `ogre_md_id`; timeline entries refer to the corresponding `data_id` and
`metadata_id`. Enabling timeline output adds a companion file while retaining
the data file. The identifiers below are illustrative.

**Example normalized timeline:**
```json
{
    "id": "1601951677310e6fd74c17191fc86a4",
    "timestamp": "2021-04-14T21:30:24.000000+00:00",
    "timestamp_meaning": "Event generation time",
    "data_type": "windows_events",
    "related_user": "S-1-5-18",
    "description": "Microsoft-Windows-Kernel-PnP:403",
    "additional_description": "device_instance_id: ROOT\\ACPI_HAL\\0000 - driver_name: hal.inf",
    "data_id": "227a391fb1b4b10a88c755e3e97ca17c",
    "metadata_id": "c74f2407393c14da9d4f62905fb75d"
}
```

## Analytics JSONL

`analytics_jsonl` wraps each data record in an envelope containing `ogre_id`,
`computer`, `data_type`, `ogre_md_id`, and `data`. The artifact fields remain
inside `data`, while the envelope supports filtering by computer or data type.
Metadata is written separately to `ogre_metadata.jsonl`.

Like normalized JSONL, enabling timeline output creates a separate
`<base>.<data_type>.tl.jsonl` file rather than replacing the data records.
`timeline_include_undated` is not supported with this format. Gzip output adds
`.gz` to each filename.

## Metadata

Each format preserves metadata describing the source of the artifact. Available
fields depend on the command and collection; a single-file plugin run identifies
its source through the supplied computer name and input filename.

It contains the following data:
- **computer**: The name of the computer,
- **data_type**: data type defined by the plugin that extracted the atefact,
- **id**: metadata identifier in normalized or analytics output,
- **orc_id**: the DFIR‑ORC run identifier,
- **orc_start_date**: the date on which DFIR‑ORC (not OGRE) was launched,  
- **archive**: source archive name,
- **subarchive**: nested archive name,
- **folder**: the archive sub folder where the extracted file is located,
- **archive_filename**: file path within the archive, or the supplied input path for a single-file plugin run,
- **original_filename**: the original file name extracted from the `GetThis.csv` file,
- **vss**: the *Volume Shadow Copy* extracted from the `GetThis.csv` file,
- **creation_date**: the original file creation date extracted from the `GetThis.csv` file,
- **modif_date**: the original file modification date extracted from the `GetThis.csv` file,
