---
 title: 'Subject Interface Package'
---


{{< callout type="important" >}}Data Type: **subject_interface_package** \
	Python Parser: **RegSIPP**{{< /callout >}}

### Description 

Extracts Subject Interface Package (SIP) records from the Windows `Software` hive. It reads each SIP’s GUID, human‑readable name, associated DLL path, and entry‑point function name, together with key metadata.

- Provides the SIP GUID, uniquely identifying the package.
- Records the DLL location that implements the SIP.
- Captures the function name used as the package's entry point.
- Includes the registry key owner SID for user association.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `name`   |
|Additional Description    | `dll`   |
|    | `function_name`   |
|    | `guid`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `name` | String |  | human‑readable name of the Subject Interface Package (SIP) identified by the GUID |
| `dll` | String | FILE_PATH | filesystem path to the DLL that implements the SIP |
| `function_name` | String |  | entry‑point function name within the DLL used for SIP verification |
| `guid` | String |  | GUID uniquely identifying the Subject Interface Package |
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
