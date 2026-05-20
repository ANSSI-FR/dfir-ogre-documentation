---
 title: 'Shellbags'
---


{{< callout type="important" >}}Data Type: **shellbags** \
	Python Parser: **RegShellBag**{{< /callout >}}

### Description 

Extracts the contents of Shell Bag structures stored in the `UsrClass` hive. These structures record directories and items that a user has browsed with Windows Explorer.

It reconstructs the hierarchical path of each bag entry, exposing the folder path, item type, name and associated registry metadata such as modification timestamps and security descriptors.

- Retrieves browsed folder paths from the registry.
- Identifies the item type (root folder, file entry, network location, etc.).


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
| `modification_time` | DateTime | DATE_MODIFICATION | last modification timestamp of the underlying file |
| `access_time` | DateTime | DATE_ACCESS | last access timestamp of the underlying file |
| `creation_time` | DateTime | DATE_CREATION | creation timestamp of the underlying file |
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
