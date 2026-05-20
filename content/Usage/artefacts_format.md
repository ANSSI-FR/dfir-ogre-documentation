---
date: '2026-01-06T15:52:05+01:00'
title: 'Artefact formats'
weight: 3
---

DFIR-OGRE provides several output format for the extracted artefacts.

## Raw format
- Created when the [output configuration](/usage/ogre_configuration/#output-section-how-to-write-extracted-artefacts) template contains:
    - `with_timeline: false`

- Data is extracted without further processing
- an `ogre_md` field contains metadata collected during extraction.
- this is the simplest format and is most suited for artefacts that does not contains dates.
**Example:**
  ```json
  {
      "ogre_md": {
        "archive": "ORC_Server_SRV-General.7z",
        "subarchive": "Event.7z",
        "computer": "SRV-HV01",
      },
      "system": {
        "time_created": {
          "system_time": "2021-04-14T21:30:24.000000Z"
        },
        "provider": {
          "provider_name": "PowerShell"
        },
      },
      "event_data": {
        "device_instance_id":"ROOT\\ACPI_HAL\\0000",
        "driver_name":"hal.inf",
      }
  }
  ```


## Timeline format
- Created when the output definition template contains:
    - `with_timeline: true`

- For each date present in the extracted artefact, a line is created that contains a **timestamp** field as well as fields summarizing the entry.  

    - For **NTFSInfo** and **USNInfo**, the meaning of the timestamp follows the MACB convention.  

- Contains all data extracted by the plugin together with the metadata.  

- It is well suited for ingestion into **Splunk** or **ELK**.  

**Example:**
```json
{
    "timestamp": "2021-04-14T21:30:24.000000+00:00",
    "timestamp_meaning": "Event generation time",
    "data_type": "win_evtx",
    "related_user": "S-1-5-18",
    "description": "Microsoft-Windows-Kernel-PnP:403",
    "additional_description": "device_instance_id: ROOT\\ACPI_HAL\\0000 - driver_name: hal.inf",
    "data": {
        "system": {
          "time_created": {
            "system_time": "2021-04-14T21:30:24.000000Z"
          },
          "provider": {
            "provider_name": "PowerShell"
          },
        },
        "event_data": {
          "device_instance_id":"ROOT\\ACPI_HAL\\0000",
          "driver_name":"hal.inf",
        }
    }
    "ogre_md": {
        "archive": "ORC_Server_SRV-General.7z",
        "subarchive": "Event.7z",
        "computer": "SRV-HV01",
    },
}
```

## Normalized formats
- The previous formats are denormalised to be easily ingested in inverted indexes like *ELK*, which results in a high degree of data duplication.  
    - metada duplication
    - data duplication when - Created when the

- Normalized formats separate the data, metadata, and timeline into distinct files; each record is linked by a unique identifier.  

- Good format for ingestion into analytical databases.  

- Created when the output definition template contains:
    - `format: normalized_jsonl`
    - or `format: normalized_csv`

**Example ot normalized timeline:**
```json
{
    "id": "1601951677310e6fd74c17191fc86a4",
    "timestamp": "2021-04-14T21:30:24.000000+00:00",
    "timestamp_meaning": "Event generation time",
    "data_type": "win_evtx",
    "related_user": "S-1-5-18",
    "description": "Microsoft-Windows-Kernel-PnP:403",
    "additional_description": "device_instance_id: ROOT\\ACPI_HAL\\0000 - driver_name: hal.inf",
    "data_id": "227a391fb1b4b10a88c755e3e97ca17c",
    "ogre_md_id": "c74f2407393c14da9d4f62905fb75d",
}
```

## Metadata

Every data format provides metada collected during the extract. It provides detailled information about where the artefact comes from.

It contains the following data:
- **computer**: The name of the computer,
- **data_type**: data type defined by the plugin that extracted the atefact,
- **id**: metadata id, if normalized format is used,
- **orc_id**: the DFIR‑ORC run identifier,
- **orc_start_date**: the date on which DFIR‑ORC (not OGRE) was launched,  
- **archive**: Option<String>,
- **subarchive**: Option<String>,
- **folder**: the archive sub folder where the extracted file is located,
- **archive_filename**: the file name in the archive,
- **original_filename**: the original file name extracted from the `GetThis.csv` file,
- **vss**: the *Volume Shadow Copy* extracted from the `GetThis.csv` file,
- **creation_date**: the original file creation date extracted from the `GetThis.csv` file,
- **modif_date**: the original file modification date extracted from the `GetThis.csv` file,
