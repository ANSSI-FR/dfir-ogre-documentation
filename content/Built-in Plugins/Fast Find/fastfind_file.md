---
 title: 'Fastfind File'
---


{{< callout type="important" >}}Data Type: **fastfind_file** \
	Python Parser: **FastFindFile**{{< /callout >}}

### Description 

Parse the filesystem results of the fastfind tool


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `fn_fullname`   |
|Additional Description    | `description`   |
|    | `i30_fullname`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `fn_fullname` | String | FILE_PATH |  |
| `i30_fullname` | String | FILE_PATH |  |
| `description` | String |  |  |
| `volume_id` | String |  |  |
| `snapshot_id` | String |  |  |
| `sequence_number` | Int |  |  |
| `record_number` | Int |  |  |
| `@frn` | Extension |  |  |
| `fn_parent_sequence_number` | Int |  |  |
| `fn_parent_record_number` | Int |  |  |
| `filename/@parentfrn` | Extension |  |  |
| `i30_parent_sequence_number` | Int |  |  |
| `i30_parent_record_number` | Int |  |  |
| `i30/@parentfrn` | Extension |  |  |
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
| `si_creation_date` | DateTime | DATE_CREATION |  |
| `si_lastmod_date` | DateTime | DATE_MODIFICATION |  |
| `si_lastaccess_date` | DateTime | DATE_ACCESS |  |
| `si_lastchange_date` | DateTime | DATE_CHANGE |  |
| `fn_creation_date` | DateTime | DATE_CREATION |  |
| `fn_lastmod_date` | DateTime | DATE_MODIFICATION |  |
| `fn_lastaccess_date` | DateTime | DATE_ACCESS |  |
| `fn_lastchange_date` | DateTime | DATE_CHANGE |  |
| `i30_creation` | DateTime | DATE_CREATION |  |
| `i30_lastmodification` | DateTime | DATE_MODIFICATION |  |
| `i30_lastaccess` | DateTime | DATE_ACCESS |  |
| `i30_lastentrychange` | DateTime | DATE_CHANGE |  |
| `data[]` | Array[Object] |  |  |
| `data[].name` | String | FILE_NAME |  |
| `data[].filesize` | Int | FILE_SIZE |  |
| `data[].md5` | String | FILE_MD5 |  |
| `data[].sha1` | String | FILE_SHA1 |  |
| `data[].sha256` | String | FILE_SHA256 |  |
