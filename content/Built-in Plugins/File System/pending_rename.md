---
 title: 'Pending Rename'
---


{{< callout type="important" >}}Data Type: **pending_rename** \
	Python Parser: **RegPendingRename**{{< /callout >}}

### Description 

Each row is a file rename or deletion operation queued in PendingFileRenameOperations for the next reboot, with source and target paths plus registry provenance. Use it to identify delayed replacement, cleanup, or persistence actions and correlate affected files. The value records intent; it does not prove that a reboot occurred or the operation completed.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `old_name`   |
|Additional Description    | `new_name`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `old_name` | String | original file path scheduled for rename at next reboot |
| `new_name` | String | target file path after rename operation |
| `key_path` | String | full registry key name |
| `key_modif_time` | DateTime | last modification timestamp of the registry key |
| `key_security` | Object |  |
| `key_security.owner_sid` | String | SID of the user that owns the registry key |
| `key_security.group_sid` | String | SID of the group that owns the registry key |
| `key_security.control_flags[]` | Array[String] | security descriptor control flags for the key |
| `key_security.sacl_aces[]` | Array[Object] |  |
| `key_security.sacl_aces[].ace_type` | String | type of ACE (e.g., allow, deny) |
| `key_security.sacl_aces[].ace_flags[]` | Array[String] | ACE flags that modify inheritance or behavior |
| `key_security.sacl_aces[].rights[]` | Array[String] | permissions granted or denied by the ACE |
| `key_security.sacl_aces[].account_sid` | String | SID of the account the ACE applies to |
| `key_security.sacl_aces[].ace_size` | Int | declared ACE size in bytes |
| `key_security.sacl_aces[].object_type_guid` | String | GUID identifying the object type governed by the ACE |
| `key_security.sacl_aces[].inherited_object_type_guid` | String | GUID identifying the inherited object type governed by the ACE |
| `key_security.sacl_aces[].raw_hex` | String | raw ACE bytes preserved as hexadecimal |
| `key_security.dacl_aces[]` | Array[Object] |  |
| `key_security.dacl_aces[].ace_type` | String | type of ACE (e.g., allow, deny) |
| `key_security.dacl_aces[].ace_flags[]` | Array[String] | ACE flags that modify inheritance or behavior |
| `key_security.dacl_aces[].rights[]` | Array[String] | permissions granted or denied by the ACE |
| `key_security.dacl_aces[].account_sid` | String | SID of the account the ACE applies to |
| `key_security.dacl_aces[].ace_size` | Int | declared ACE size in bytes |
| `key_security.dacl_aces[].object_type_guid` | String | GUID identifying the object type governed by the ACE |
| `key_security.dacl_aces[].inherited_object_type_guid` | String | GUID identifying the inherited object type governed by the ACE |
| `key_security.dacl_aces[].raw_hex` | String | raw ACE bytes preserved as hexadecimal |
