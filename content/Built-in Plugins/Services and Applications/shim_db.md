---
 title: 'Shim Db'
---


{{< callout type="important" >}}Data Type: **shim_db** \
	Python Parser: **RegShimDb**{{< /callout >}}

### Description 

Extracts information about the Windows Application Compatibility Shim database stored in the `Software` hive. .

- Lists each shim database GUID with the registry keys that reference it.
- Provides the installation timestamp and the physical file path of the shim database.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `target`   |
|Additional Description    | `file_path`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `file_path` | String | FILE_PATH | filesystem path entry in the shim database file |
| `install_time` | DateTime | DATE_INSTALLATION | timestamp when the entry was installed |
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
