---
 title: 'Mui Cache'
---


{{< callout type="important" >}}Data Type: **mui_cache** \
	Python Parser: **RegMuiCache**{{< /callout >}}

### Description 

Extracts entries from the per‑user MUI cache stored in the `Registry` hive.

- Provides executable name and its human‑readable description.


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
| `key_security.dacl_ace` | Object |  |  |
| `key_security.dacl_ace.ace_type` | String |  | type of ACE (e.g., allow, deny) |
| `key_security.dacl_ace.account_sid` | String |  | SID of the account the ACE applies to |
| `key_security.dacl_ace.ace_flags[]` | Array[String] |  | ACE flags that modify inheritance or behavior |
| `key_security.dacl_ace.rights[]` | Array[String] |  | permissions granted or denied by the ACE |
