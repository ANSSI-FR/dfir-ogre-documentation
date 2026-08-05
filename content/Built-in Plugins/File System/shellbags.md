---
 title: 'Shellbags'
---


{{< callout type="important" >}}Data Type: **shellbags** \
	Python Parser: **RegShellBag**{{< /callout >}}

### Description 

Each row reconstructs a folder or item recorded in a user's Shellbag hierarchy, with browsed path, item type and name, embedded timestamps, and registry provenance. Use it to infer Explorer awareness of folders, including removable or network locations, and correlate paths with other user artifacts. Times belong to item or Registry structures rather than a guaranteed visit event; local DOS or FAT times are normalized with the matching SYSTEM hive.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `path`   |
|Additional Description    | `type`   |
|    | `name`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `name` | String |  | displayed name of the shell item (folder, file, volume, etc.) |
| `type` | String |  | type identifier of the shell item (e.g., control_panel_category, network_location, file_entry) |
| `localized_name` | String |  | localized (human‑readable) name of a file entry, if present in the extension block |
| `file_reference` | String |  | NTFS file reference (MFT entry) of the file, formatted as 'MFT‑Sequence‑Index' |
| `path` | String |  | reconstructed hierarchical path derived from the shell bag entry |
| `description` | String |  | textual description associated with a network location item |
| `comments` | String |  | user‑defined comments attached to a network location item |
| `modification_time` | DateTime | DATE_MODIFICATION | UTC modification timestamp converted from the shell item's DOS/FAT local time using the matching SYSTEM hive |
| `access_time` | DateTime | DATE_ACCESS | UTC access timestamp converted from the shell item's DOS/FAT local time using the matching SYSTEM hive |
| `creation_time` | DateTime | DATE_CREATION | UTC creation timestamp converted from the shell item's DOS/FAT local time using the matching SYSTEM hive |
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
