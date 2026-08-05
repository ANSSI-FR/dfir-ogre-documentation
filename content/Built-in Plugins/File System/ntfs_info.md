---
 title: 'Ntfs Info'
---


{{< callout type="important" >}}Data Type: **ntfsinfo** \
	Python Parser: **NTFSInfo**{{< /callout >}}

### Description 

Each row represents an NTFS Master File Table record exported by ORC, with path, file and parent identifiers, standard and filename timestamps, attributes, size, hashes, and executable metadata. Use it to reconstruct filesystem state and correlate binaries or deleted records. NTFS timestamps can be altered or inherited and do not by themselves identify the actor or action.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `file_path`   |
|Additional Description    | `file_size`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `snapshot_id` | Python | Volume snapshot the file was collected from |
| `parent` | String | full parent directory path of the entry |
| `file_name` | String | name of the file without path |
| `extension` | String | file extension (e.g., .txt, .exe) |
| `file_size` | Int | size of the file in bytes |
| `file_in_use` | Bool | flag indicating whether the MFT record is allocated (true) or free (false) |
| `sequence_number` | Int | sequence number part of the File Reference Number (FRN) |
| `record_number` | Int | record/index part of the File Reference Number (FRN) |
| `FRN` | Extension |  |
| `file_attributes_archive` | Bool | archive attribute flag |
| `file_attributes_no_scrub_data` | Bool | no‑scrub‑data attribute flag |
| `file_attributes_compressed` | Bool | compressed attribute flag |
| `file_attributes_directory` | Bool | directory attribute flag |
| `file_attributes_encrypted` | Bool | encrypted attribute flag |
| `file_attributes_hidden` | Bool | hidden attribute flag |
| `file_attributes_not_content_indexed` | Bool | not‑content‑indexed attribute flag |
| `file_attributes_reparse_point` | Bool | reparse‑point attribute flag |
| `file_attributes_normal` | Bool | normal attribute flag |
| `file_attributes_offline` | Bool | offline attribute flag |
| `file_attributes_sparse_file` | Bool | sparse‑file attribute flag |
| `file_attributes_readonly` | Bool | read‑only attribute flag |
| `file_attributes_system` | Bool | system attribute flag |
| `file_attributes_temporary` | Bool | temporary attribute flag |
| `file_attributes_virtual` | Bool | virtual attribute flag |
| `file_attributes_recall_on_data_access` | Bool | recall‑on‑data‑access attribute flag |
| `file_attributes_device` | Bool | device attribute flag |
| `file_attributes_ea` | Bool | extended‑attributes (EA) attribute flag |
| `file_attributes_recall_on_open` | Bool | recall‑on‑open attribute flag |
| `file_attributes_pinned` | Bool | pinned attribute flag |
| `file_attributes_integrity_stream` | Bool | integrity‑stream attribute flag |
| `file_attributes_unpinned` | Bool | unpinned attribute flag |
| `Attributes` | Extension |  |
| `usn_number` | IntRadix | USN journal sequence number (hexadecimal) |
| `file_name_flags` | Int | flags associated with the filename entry |
| `fn_creation_date` | DateTime | creation timestamp of the filename entry |
| `fn_lastmod_date` | DateTime | last modification timestamp of the filename entry |
| `fn_lastaccess_date` | DateTime | last access timestamp of the filename entry |
| `fn_lastchange_date` | DateTime | timestamp of the last attribute change for the filename entry |
| `si_creation_date` | DateTime | creation timestamp of the file |
| `si_lastmod_date` | DateTime | last modification timestamp of the file |
| `si_lastaccess_date` | DateTime | last access timestamp of the file |
| `si_lastchange_date` | DateTime | timestamp of the last attribute change for the file |
| `md5` | String | MD5 hash of the file content |
| `sha1` | String | SHA‑1 hash of the file content |
| `sha256` | String | SHA‑256 hash of the file content |
| `orc_pe_md5` | String | MD5 hash of the PE executable (if file is a PE) |
| `orc_pe_sha1` | String | SHA‑1 hash of the PE executable (if file is a PE) |
| `orc_pe_sha256` | String | SHA‑256 hash of the PE executable (if file is a PE) |
| `file_pe_md5` | String | MD5 hash extracted from the Authenticode‑signed PE file |
| `file_pe_sha1` | String | SHA‑1 hash extracted from the Authenticode‑signed PE file |
| `file_pe_sha256` | String | SHA‑256 hash extracted from the Authenticode‑signed PE file |
| `SignedHash` | Extension |  |
| `authenticode_signer` | String | subject name of the Authenticode signing certificate |
| `authenticode_signer_thumbprint` | Split | thumbprint(s) of the Authenticode signing certificate |
| `authenticode_ca` | String | certificate authority that issued the signing certificate |
| `authenticode_ca_thumbprint` | Split | thumbprint(s) of the signing certificate authority |
| `authenticode_status` | String | verification status of the Authenticode signature (e.g., valid, invalid) |
| `pe_version` | String | version string of the PE file (FileVersion) |
| `pe_companyname` | String | company name embedded in the PE metadata |
| `pe_productname` | String | product name embedded in the PE metadata |
| `pe_original_filename` | String | original filename stored in the PE metadata |
| `pe_platform` | String | target platform/architecture of the PE (e.g., x86, x64) |
| `pe_compilation_date` | DateTime | compilation timestamp of the PE executable |
| `pe_subsystem` | String | subsystem type defined in the PE header (e.g., GUI, Console) |
