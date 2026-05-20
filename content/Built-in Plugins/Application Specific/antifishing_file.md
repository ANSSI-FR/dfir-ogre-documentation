---
 title: 'Antifishing File'
---


{{< callout type="important" >}}Data Type: **antifishing_file** \
	Python Parser: **RegAntifishingFile**{{< /callout >}}

### Description 

Extracts the Internet Explorer anti‑phishing registry hive under `NTUser` hive.

- Extracts the `UserFile` value and the key’s security descriptor, exposing the file used for IE’s anti‑phishing feature and the owning user.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `user_file`   |
|Additional Description    | `order_index`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `user_file` | String | FILE_PATH | Path to the file used by Internet Explorer's anti‑phishing feature |
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
