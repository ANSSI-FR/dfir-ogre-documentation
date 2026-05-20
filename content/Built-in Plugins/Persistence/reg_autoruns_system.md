---
 title: 'Reg Autoruns System'
---


{{< callout type="important" >}}Data Type: **reg_autoruns** \
	Python Parser: **RegAutorunsSystem**{{< /callout >}}

### Description 

Extracts persistence‑related registry data from the SYSTEM hive.
- Enumerates well‑known keys that are used by Windows and third‑party software
  to achieve automatic execution (autoruns).
- Groups the data by a *persistence type* (e.g., “Session Manager *Execute”,
  “Network Providers”, etc.) and returns the values found under each key.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `type`   |
|    | `key_path`   |
|Additional Description    | `values`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `type` | String |  | Logical name of the persistence mechanism (e.g., 'Session Manager *Execute') |
| `values[]` | Array[Object] |  | value set extracted from the registry key. |
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
