---
 title: 'User Assist'
---


{{< callout type="important" >}}Data Type: **user_assist** \
	Python Parser: **RegUserAssist**{{< /callout >}}

### Description 

Each row is a per-user UserAssist record for a GUI-launched item, with decoded path or name, run count, focus metrics, launch type, last-run time, and registry provenance. Use it as execution evidence and correlate user-attributed launches with files and other timelines. Counter semantics vary by format and Windows version, and absence does not exclude execution by other mechanisms.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `program_name`   |
|Additional Description    | `run`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `program_name` | String |  | decoded name of the executed program or known‑folder path |
| `launch_type` | String |  | type of launch for legacy UserAssist entries (e.g., UEME) |
| `run` | Int |  | total number of times the program was executed |
| `focus_count` | Int |  | number of times the program window received focus |
| `focus_time` | String |  | cumulative focus duration (formatted as a time delta) |
| `session` | Int |  | identifier of the logon session in which the program ran |
| `last_executed` | DateTime | DATE_LAST_RUN | timestamp of the most recent execution of the program |
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
