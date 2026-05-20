---
 title: 'Clsid'
---


{{< callout type="important" >}}Data Type: **clsid** \
	Python Parser: **RegClsIdIUser**{{< /callout >}}

### Description 

Enumerates every user‑specific COM class identifier (CLSID) stored in the `UsrClass` hive.

- Provides a complete list of per‑user COM registrations.
- Captures the executable that implements the COM object.
- Records any alternate CLSID mapping via “TreatAs”.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `description`   |
|Additional Description    | `executable`   |
|    | `treat_as`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `guid` | String | APP_CLSID | lower‑cased CLSID identifying the COM class |
| `description` | String |  | human‑readable description of the COM class |
| `executable` | String | FILE_PATH | path(s) to the binary(ies) implementing the CLSID (e.g., InprocServer32, LocalServer32) |
| `treat_as` | String | APP_CLSID | CLS ID that this entry redirects to via TreatAs |
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
