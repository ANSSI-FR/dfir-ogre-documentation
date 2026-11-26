---
 title: 'MFT'
---


{{< callout type="important" >}}Data Type: **mft** \
	Python Parser: **MFT**{{< /callout >}}

### Description 

Extracts MFT file records from a standalone raw $MFT. Output fields and qualifiers follow NTFSInfo naming scheme. 
      
It includes deleted records, sequence-aware reconstructed paths, $SI/$FN timestamps, file attributes, logical stream sizes, ADS metadata and USN. 

Unknown parent chains use *\$OrphanFiles*.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `file_path`   |
|Additional Description    | `file_size`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `file_path` | String | full path (path+name) of the file, rebuilt from the parent chain |
| `parent` | String | full parent directory path of the entry (orphaned records are under \$OrphanFiles) |
| `file_name` | String | name of the file without path |
| `extension` | String | file extension (e.g., .txt, .exe) |
| `file_size` | Int | logical size of the unnamed data stream in bytes, absent when unknown |
| `file_in_use` | Bool | flag indicating whether the MFT record is allocated (true) or free (false) |
| `sequence_number` | Int | sequence number of the MFT record |
| `record_number` | Int | index of the MFT record |
| `parent_sequence_number` | Int | sequence number of the parent directory reference |
| `parent_record_number` | Int | record number of the parent directory |
| `hard_link_count` | Int | hard link count stored in the MFT record header |
| `short_name` | String | DOS 8.3 alias when it can be associated unambiguously with this link |
| `ads[]` | Array[Object] | alternate data streams as name/size objects; an empty array when none are found; CSV stores the array as JSON in one cell |
| `ads[].name` | String | alternate data stream name |
| `ads[].size` | UInt | logical stream size in bytes; null when VCN-0 metadata is unavailable (omitted from JSONL when empty fields are disabled) |
| `file_attribute_raw` | String | raw FILE_ATTRIBUTE bitmask in hexadecimal, including unknown bits |
| `file_attributes_archive` | Bool | archive attribute flag |
| `file_attributes_no_scrub_data` | Bool | no-scrub-data attribute flag |
| `file_attributes_compressed` | Bool | compressed attribute flag |
| `file_attributes_directory` | Bool | true when the MFT record is a directory |
| `file_attributes_encrypted` | Bool | encrypted attribute flag |
| `file_attributes_hidden` | Bool | hidden attribute flag |
| `file_attributes_not_content_indexed` | Bool | not-content-indexed attribute flag |
| `file_attributes_reparse_point` | Bool | reparse-point attribute flag |
| `file_attributes_normal` | Bool | normal attribute flag |
| `file_attributes_offline` | Bool | offline attribute flag |
| `file_attributes_sparse_file` | Bool | sparse-file attribute flag |
| `file_attributes_readonly` | Bool | read-only attribute flag |
| `file_attributes_system` | Bool | system attribute flag |
| `file_attributes_temporary` | Bool | temporary attribute flag |
| `file_attributes_virtual` | Bool | virtual attribute flag |
| `file_attributes_recall_on_data_access` | Bool | recall-on-data-access attribute flag |
| `file_attributes_device` | Bool | device attribute flag |
| `file_attributes_ea` | Bool | EA / recall-on-open shared bit (0x40000); a raw MFT cannot distinguish these aliases |
| `file_attributes_pinned` | Bool | pinned attribute flag |
| `file_attributes_integrity_stream` | Bool | integrity-stream attribute flag |
| `file_attributes_recall_on_open` | Bool | recall-on-open / EA shared bit (0x40000); a raw MFT cannot distinguish these aliases |
| `file_attributes_unpinned` | Bool | unpinned attribute flag |
| `usn_number` | Int | last USN of the record, from $STANDARD_INFORMATION |
| `owner_id` | Int | owner identifier from $STANDARD_INFORMATION |
| `security_id` | Int | security descriptor identifier from $STANDARD_INFORMATION |
| `file_name_flags` | Int | $FILE_NAME namespace (0 POSIX, 1 Win32, 2 DOS, 3 Win32 and DOS) |
| `fn_creation_date` | DateTime | creation timestamp of the $FILE_NAME attribute |
| `fn_lastmod_date` | DateTime | last modification timestamp of the $FILE_NAME attribute |
| `fn_lastaccess_date` | DateTime | last access timestamp of the $FILE_NAME attribute |
| `fn_lastchange_date` | DateTime | MFT record change timestamp of the $FILE_NAME attribute |
| `si_creation_date` | DateTime | creation timestamp of the $STANDARD_INFORMATION attribute |
| `si_lastmod_date` | DateTime | last modification timestamp of the $STANDARD_INFORMATION attribute |
| `si_lastaccess_date` | DateTime | last access timestamp of the $STANDARD_INFORMATION attribute |
| `si_lastchange_date` | DateTime | MFT record change timestamp of the $STANDARD_INFORMATION attribute |
