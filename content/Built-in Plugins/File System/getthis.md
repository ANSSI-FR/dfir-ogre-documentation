---
 title: 'Getthis'
---


{{< callout type="important" >}}Data Type: **getthis** \
	Python Parser: **GetThis**{{< /callout >}}

### Description 

Each row describes a file selected by ORC GetThis, with source path, volume and snapshot, NTFS identifiers and timestamps, size, hashes, match reason, and YARA result where available. Use it to connect collected content to its original filesystem context. Selection reflects collection rules rather than a complete inventory, and collection time is distinct from file timestamps.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `full_name`   |
|Additional Description    | `file_size`   |
|    | `sequence_number`   |
|    | `record_number`   |
|    | `parent_sequence_number`   |
|    | `parent_record_number`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `volume_id` | String |  | identifier of the volume that contains the file |
| `parent_sequence_number` | Int |  | sequence part of the parent FRN |
| `parent_record_number` | Int |  | record part of the parent FRN |
| `ParentFRN` | Extension |  | file reference number (FRN) of the parent directory |
| `sequence_number` | Int |  | sequence part of the FRN |
| `record_number` | Int |  | record part of the FRN |
| `FRN` | Extension |  | file reference number (FRN) of the file itself |
| `full_name` | String |  | full absolute path of the collected file |
| `sample_name` | String |  | name of the sample or collection set the file belongs to |
| `file_size` | Int | FILE_SIZE | size of the file in bytes |
| `find_match` | String |  | string used to match the file during collection |
| `content_type` | String |  | MIME type of the file content |
| `sample_collection_date` | DateTime | DATE_MODIFICATION | timestamp when the sample was collected |
| `fn_creation_date` | DateTime | DATE_CREATION | file name creation timestamp |
| `fn_lastmod_date` | DateTime | DATE_MODIFICATION | file name modification timestamp |
| `fn_lastaccess_date` | DateTime | DATE_ACCESS | file name access timestamp |
| `fn_lastchange_date` | DateTime | DATE_CHANGE | file name modification timestamp |
| `si_creation_date` | DateTime | DATE_CREATION | creation timestamp of the file |
| `si_lastmod_date` | DateTime | DATE_MODIFICATION | last modification timestamp of the file |
| `si_lastaccess_date` | DateTime | DATE_ACCESS | last access timestamp of the file |
| `si_lastchange_date` | DateTime | DATE_MODIFICATION | last attribute‑change timestamp of the file |
| `md5` | String | FILE_MD5 | MD5 hash of the file |
| `sha1` | String | FILE_SHA1 | SHA‑1 hash of the file |
| `sha256` | String | FILE_SHA256 | SHA‑256 hash of the file |
| `attr_type` | String |  | type of the NTFS attribute |
| `attr_name` | String |  | name of the NTFS attribute |
| `attr_id` | Int |  | numeric identifier of the NTFS attribute |
| `snapshot_id` | Python |  | identifier of the snapshot from which the file was extracted |
| `ss_deep` | String |  | ssdeep fuzzy hash of the file |
| `tlsh` | String |  | TLSH hash of the file |
| `yara_rules` | String |  | YARA rule(s) that matched the file |
| `record_in_use` | String |  | flag indicating whether the MFT record is currently in use |
