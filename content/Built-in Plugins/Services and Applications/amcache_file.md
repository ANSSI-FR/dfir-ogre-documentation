---
 title: 'Amcache File'
---


{{< callout type="important" >}}Data Type: **amcache_file** \
	Python Parser: **RegAmCacheFile**{{< /callout >}}

### Description 

Retrieves cached executable file metadata from the Windows `AmCache` hive.

- Expose what the OS stores for quick access to recently used files.
- Extracts file name, path, size, SHA‑1 hash, program identifiers, version info, timestamps, and security descriptors for forensic examination.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `path`   |
|Additional Description    | `sha1`   |
|    | `size`   |
|    | `program_id`   |
|    | `key_path`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `name` | String | FILE_NAME | filename |
| `path` | String | FILE_PATH | file path |
| `size` | Int | FILE_SIZE | size in bytes |
| `program_id` | String | APP_ID | program ID, if it exists |
| `sha1` | String | FILE_SHA1 | SHA-1 hash of the file |
| `product_name` | String | PRODUCT | Product name |
| `company_name` | String | COMPANY | Company name |
| `product_version` | String | PE_VERSION | Product version |
| `version_language` | Int |  | Microsoft Language ID in decimal |
| `short_name` | String |  | ShortName of the file as found in the MFT |
| `original_filename` | String | FILE_NAME | Original FileName field of the PE header |
| `file_version` | String | PE_VERSION | File version |
| `image_size` | Int |  | 'SizeOfImage' field of the PE header |
| `file_description` | String |  | file description |
| `linker_version` | String | PE_VERSION | combination of the 'MajorLinkerVersion' and 'MinorLinkerVersion' fields of the PE header |
| `link_date` | DateTime | DATE_COMPILATION | Compilation date |
| `binary_type` | String |  | 32BIT or 64BIT |
| `creation_date` | DateTime | DATE_CREATION |  |
| `modification_date` | DateTime | DATE_MODIFICATION |  |
| `long_path_hash` | String | FILE_PATH_SHA1 | SHA-1 of the complete lowercase file path in UTF-16 |
| `unique_id` | String |  | identifies the file location if it is in a program installation directory |
| `volume_guid` | String | VOLUME_GUID | identifier of the volume where the file is located |
| `is_pe_file` | Bool |  |  |
| `is_os_component` | Bool |  |  |
| `key_path` | String | KEY_PATH | full registry key name |
| `key_modif_time` | DateTime | DATE_MODIFICATION | last modification timestamp of the registry key |
| `key_security` | Object |  |  |
| `key_security.owner_sid` | String | USER_SID | SID of the user that owns the registry key |
| `key_security.group_sid` | String |  | SID of the group that owns the registry key |
| `key_security.control_flags[]` | Array[String] |  | security descriptor control flags for the key |
| `key_security.dacl_ace` | Object |  |  |
| `key_security.dacl_ace.ace_type` | String |  | type of ACE (e.g., allow, deny) |
| `key_security.dacl_ace.account_sid` | String |  | SID of the account the ACE applies to |
| `key_security.dacl_ace.ace_flags[]` | Array[String] |  | ACE flags that modify inheritance or behavior |
| `key_security.dacl_ace.rights[]` | Array[String] |  | permissions granted or denied by the ACE |
