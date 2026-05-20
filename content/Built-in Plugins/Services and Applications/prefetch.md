---
 title: 'Prefetch'
---


{{< callout type="important" >}}Data Type: **prefetch** \
	Python Parser: **Prefetch**{{< /callout >}}

### Description 

Parses Windows Prefetch files to extract execution metadata. It shows when and how often an executable ran, which supporting files were loaded, and storage details of the volumes involved.

- Identifies the executable name and version.
- Records the number of executions and the most recent run timestamp.
- Lists files and volumes referenced by the executable.
- Captures path hints that may point to additional artefacts.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `executable`   |
|Additional Description    | `path_hints`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `executable` | String | FILE_NAME | executable file name |
| `version` | String |  | version |
| `prefetch_hash` | Int |  | hash identifier of the prefetch file |
| `run_count` | Int |  | number of times the executable was run |
| `run_date` | DateTime | DATE_LAST_RUN | timestamp of the most recent execution |
| `file_count` | Int |  | count of file entries referenced by the prefetch |
| `files[]` | Array[Object] |  |  |
| `files[].index` | Int |  | index of the file entry |
| `files[].path` | String | FILE_PATH | full path of a referenced file |
| `files[].frn` | String |  | file reference number (FRN) in hexadecimal |
| `files[].sequence_number` | Int | MFT_SEQUENCE | sequence component of the FRN |
| `files[].record_number` | Int | FS_INODE | record/inode component of the FRN |
| `volume_count` | Int |  | number of volumes referenced |
| `volumes[]` | Array[Object] |  |  |
| `volumes[].path` | String |  | device path of the volume |
| `volumes[].serial_number` | Int |  | volume serial number |
| `volumes[].creation_time` | DateTime |  | creation timestamp of the volume |
| `path_hints[]` | Array[String] |  | relative paths within volumes that hint at additional artefacts |
