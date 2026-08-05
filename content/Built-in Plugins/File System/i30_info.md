---
 title: 'I30 info'
---


{{< callout type="important" >}}Data Type: **i30info** \
	Python Parser: **I30Info**{{< /callout >}}

### Description 

Each row represents a current or carved NTFS directory-index entry, with name, reconstructed path, file and parent record identifiers, timestamps, size, attributes, volume, and snapshot. Use it to recover directory membership and possible deleted-name remnants. Carved records and embedded timestamps require corroboration, and a directory entry alone does not prove user interaction.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `name`   |
|Additional Description    | `file_size`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `name` | String | File Name |
| `file_size` | Int | size of the file in bytes |
| `flags` | String | File Name Flag |
| `is_carved` | String | Whether this entry have been carved or not |
| `sequence_number` | Int | sequence number part of the File Reference Number (FRN) |
| `record_number` | Int | record/index part of the File Reference Number (FRN) |
| `FRN` | Extension |  |
| `parent_sequence_number` | Int | sequence number part of the File Reference Number (FRN) |
| `parent_record_number` | Int | record/index part of the File Reference Number (FRN) |
| `ParentFRN` | Extension |  |
| `volume_id` | String | Volume identifier |
| `snapshot_id` | Python |  |
| `fn_creation_date` | DateTime | creation timestamp of the filename entry |
| `fn_lastmod_date` | DateTime | last modification timestamp of the filename entry |
| `fn_lastaccess_date` | DateTime | last access timestamp of the filename entry |
| `fn_lastchange_date` | DateTime | timestamp of the last attribute change for the filename entry |
