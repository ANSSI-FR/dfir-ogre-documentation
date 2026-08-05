---
 title: 'Amcache Files'
---


{{< callout type="important" >}}Data Type: **amcache_file** \
	Python Parser: **RegAmCacheFile**{{< /callout >}}

### Description 

Each row is a file inventory record from the Amcache hive, with path, normalized hash, size, program identifiers, version or publisher data, timestamps, and registry provenance. Use it to identify binaries and correlate software across files, programs, and hosts. Amcache presence is contextual inventory evidence, not standalone proof of execution, and schema semantics vary by Windows version.


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
| `file_id` | String |  | raw Amcache FileId or legacy value 101 |
| `sha1` | String | FILE_SHA1 | normalized 40-hex SHA-1 hash of the file |
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
| `key_security.sacl_aces[]` | Array[Object] |  |  |
| `key_security.sacl_aces[].ace_type` | String |  | type of ACE (e.g., allow, deny) |
| `key_security.sacl_aces[].ace_flags[]` | Array[String] |  | ACE flags that modify inheritance or behavior |
| `key_security.sacl_aces[].rights[]` | Array[String] |  | permissions granted or denied by the ACE |
| `key_security.sacl_aces[].account_sid` | String |  | SID of the account the ACE applies to |
| `key_security.sacl_aces[].ace_size` | Int |  | declared ACE size in bytes |
| `key_security.sacl_aces[].object_type_guid` | String |  | GUID identifying the object type governed by the ACE |
| `key_security.sacl_aces[].inherited_object_type_guid` | String |  | GUID identifying the inherited object type governed by the ACE |
| `key_security.sacl_aces[].raw_hex` | String |  | raw ACE bytes preserved as hexadecimal |
| `key_security.dacl_aces[]` | Array[Object] |  |  |
| `key_security.dacl_aces[].ace_type` | String |  | type of ACE (e.g., allow, deny) |
| `key_security.dacl_aces[].ace_flags[]` | Array[String] |  | ACE flags that modify inheritance or behavior |
| `key_security.dacl_aces[].rights[]` | Array[String] |  | permissions granted or denied by the ACE |
| `key_security.dacl_aces[].account_sid` | String |  | SID of the account the ACE applies to |
| `key_security.dacl_aces[].ace_size` | Int |  | declared ACE size in bytes |
| `key_security.dacl_aces[].object_type_guid` | String |  | GUID identifying the object type governed by the ACE |
| `key_security.dacl_aces[].inherited_object_type_guid` | String |  | GUID identifying the inherited object type governed by the ACE |
| `key_security.dacl_aces[].raw_hex` | String |  | raw ACE bytes preserved as hexadecimal |
