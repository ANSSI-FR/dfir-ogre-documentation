---
 title: 'Mui Cache'
---


{{< callout type="important" >}}Data Type: **mui_cache** \
	Python Parser: **RegMuiCache**{{< /callout >}}

### Description 

Each row is a per-user MUI cache association between an executable path and its display description, with registry path, owner, and key LastWrite time. Use it to discover binaries exposed to the shell and attribute cached metadata to a profile. Cache presence is not standalone proof that the executable ran, and LastWrite is key-level.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `executable`   |
|Additional Description    | `description`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `executable` | String |  | executable name (including extension) as stored in the per‑user MUI cache |
| `description` | String |  | human‑readable description of the executable  |
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
