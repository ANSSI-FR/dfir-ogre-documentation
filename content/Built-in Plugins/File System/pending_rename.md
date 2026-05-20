---
 title: 'Pending Rename'
---


{{< callout type="important" >}}Data Type: **pending_rename** \
	Python Parser: **RegPendingRename**{{< /callout >}}

### Description 

Extracts entries from the `PendingFileRenameOperations` value in the `System` hive. It lists file rename operations that Windows will perform on the next reboot, capturing the original and target paths.

- Shows which files are scheduled for rename at startup.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `old_name`   |
|Additional Description    | `new_name`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `old_name` | String |  | original file path scheduled for rename at next reboot |
| `new_name` | String |  | target file path after rename operation |
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
