---
 title: 'Prefetch'
---


{{< callout type="important" >}}Data Type: **prefetch** \
	Python Parser: **Prefetch**{{< /callout >}}

### Description 

Each row describes a Windows Prefetch file for an executable, with executable name, prefetch version and hash, run count, recorded run times, referenced files, and source volumes. Use it as strong execution evidence and to correlate paths, devices, and supporting files. Creation depends on Windows configuration and workload, retention is limited, and absence does not prove non-execution.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `executable`   |
|Additional Description    | `path_hints`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `executable` | String | executable file name |
| `version` | String | version |
| `prefetch_hash` | Int | hash identifier of the prefetch file |
| `run_count` | Int | number of times the executable was run |
| `run_date` | DateTime | timestamp of the most recent execution |
| `file_count` | Int | count of file entries referenced by the prefetch |
| `files[]` | Array[Object] |  |
| `files[].index` | Int | index of the file entry |
| `files[].path` | String | full path of a referenced file |
| `files[].frn` | String | file reference number (FRN) in hexadecimal |
| `files[].sequence_number` | Int | sequence component of the FRN |
| `files[].record_number` | Int | record/inode component of the FRN |
| `volume_count` | Int | number of volumes referenced |
| `volumes[]` | Array[Object] |  |
| `volumes[].path` | String | device path of the volume |
| `volumes[].serial_number` | Int | volume serial number |
| `volumes[].creation_time` | DateTime | creation timestamp of the volume |
| `path_hints[]` | Array[String] | relative paths within volumes that hint at additional artefacts |
