---
 title: 'Usninfo'
---


{{< callout type="important" >}}Data Type: **usninfo** \
	Python Parser: **USNInfo**{{< /callout >}}

### Description 

Parses the CSV export of the Windows USN Journal. It extracts metadata for every change to a file or directory. Each entry provides identifiers, timestamps, attribute flags and the reason for the change.

- Reveals the exact moment a file was created, modified, deleted or renamed.
- Supplies the unique FRN (File Reference Number) split into sequence / record numbers, enabling correlation of multiple events for the same object.
- Lists granular attribute flags (archive, hidden, system, etc.) and change reasons (e.g., data write, security change).


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `file_path`   |
|Additional Description    | `sequence_number`   |
|    | `record_number`   |
|    | `parent_sequence_number`   |
|    | `parent_record_number`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `computer_name` | String |  | name of the host that generated the USN record |
| `usn_number` | IntRadix | FS_USN | USN (Update Sequence Number) in hexadecimal |
| `sequence_number` | Int |  | sequence part of the FRN |
| `record_number` | Int |  | record part of the FRN |
| `FRN` | Extension |  |  |
| `parent_sequence_number` | Int |  | sequence part of the parent FRN |
| `parent_record_number` | Int |  | record part of the parent FRN |
| `ParentFRN` | Extension |  |  |
| `timestamp` | DateTime |  | timestamp of the change recorded in the USN journal |
| `file` | String | FILE_NAME | name of the file or directory (no path) |
| `file_path` | String | FILE_PATH | full path of the file or directory |
| `file_attributes_archive` | Bool |  | archive attribute flag |
| `file_attributes_no_scrub_data` | Bool |  | no‑scrub‑data attribute flag |
| `file_attributes_compressed` | Bool |  | compressed attribute flag |
| `file_attributes_directory` | Bool |  | directory attribute flag |
| `file_attributes_encrypted` | Bool |  | encrypted attribute flag |
| `file_attributes_hidden` | Bool |  | hidden attribute flag |
| `file_attributes_not_content_indexed` | Bool |  | not‑content‑indexed attribute flag |
| `file_attributes_reparse_point` | Bool |  | reparse‑point attribute flag |
| `file_attributes_normal` | Bool |  | normal attribute flag |
| `file_attributes_offline` | Bool |  | offline attribute flag |
| `file_attributes_sparse_file` | Bool |  | sparse‑file attribute flag |
| `file_attributes_readonly` | Bool |  | read‑only attribute flag |
| `file_attributes_system` | Bool |  | system attribute flag |
| `file_attributes_temporary` | Bool |  | temporary attribute flag |
| `file_attributes_virtual` | Bool |  | virtual attribute flag |
| `file_attributes_recall_on_data_access` | Bool |  | recall‑on‑data‑access attribute flag |
| `file_attributes_device` | Bool |  | device attribute flag |
| `file_attributes_ea` | Bool |  | extended‑attributes (EA) attribute flag |
| `file_attributes_recall_on_open` | Bool |  | recall‑on‑open attribute flag |
| `file_attributes_pinned` | Bool |  | pinned attribute flag |
| `file_attributes_integrity_stream` | Bool |  | integrity‑stream attribute flag |
| `file_attributes_unpinned` | Bool |  | unpinned attribute flag |
| `file_name_flags` | Extension |  |  |
| `reason` | Split |  | reason codes describing why the USN entry was generated |
| `volume_id` | String |  | identifier of the volume on which the change occurred |
| `snapshot_id` | String |  | identifier of the volume snapshot (if applicable) |
