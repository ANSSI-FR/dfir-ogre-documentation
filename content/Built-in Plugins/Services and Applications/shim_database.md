---
 title: 'Shim Database'
---


{{< callout type="important" >}}Data Type: **shim_db** \
	Python Parser: **RegShimDb**{{< /callout >}}

### Description 

Each row identifies an installed Windows application-compatibility shim database, with database GUID, file path, install time, and registry provenance. Use it to find custom compatibility layers that may alter application behavior or provide persistence and correlate the database file. Installation can be legitimate and does not prove the shim was applied to a specific process.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `target`   |
|Additional Description    | `file_path`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `file_path` | String | filesystem path entry in the shim database file |
| `target[]` | Array[String] | application compatibility target path associated with the shim database |
| `install_time` | DateTime | timestamp when the entry was installed |
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
