---
 title: 'I30Info'
---


{{< callout type="important" >}}Data Type: **i30info** \
	Python Parser: **I30Info**{{< /callout >}}

### Description 

Extract NTFS's $i30 informations from an ORC‑generated CSV file.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `name`   |
|Additional Description    | `file_size`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `name` | String |  | File Name |
| `file_size` | Int | FILE_SIZE | size of the file in bytes |
| `flags` | String |  | File Name Flag |
| `is_carved` | String |  | Whether this entry have been carved or not |
| `sequence_number` | Int |  | sequence number part of the File Reference Number (FRN) |
| `record_number` | Int |  | record/index part of the File Reference Number (FRN) |
| `FRN` | Extension |  |  |
| `parent_sequence_number` | Int |  | sequence number part of the File Reference Number (FRN) |
| `parent_record_number` | Int |  | record/index part of the File Reference Number (FRN) |
| `ParentFRN` | Extension |  |  |
| `volume_id` | String |  | Volume identifier |
| `snapshot_id` | Python |  |  |
| `fn_creation_date` | DateTime | DATE_CREATION | creation timestamp of the filename entry |
| `fn_lastmod_date` | DateTime | DATE_MODIFICATION | last modification timestamp of the filename entry |
| `fn_lastaccess_date` | DateTime | DATE_ACCESS | last access timestamp of the filename entry |
| `fn_lastchange_date` | DateTime | DATE_CHANGE | timestamp of the last attribute change for the filename entry |
