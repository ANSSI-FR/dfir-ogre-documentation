---
 title: 'User Profile'
---


{{< callout type="important" >}}Data Type: **user_profile** \
	Python Parser: **RegUserProfile**{{< /callout >}}

### Description 

Extracts data about Windows user profiles from the `Software` hive.

- Lists all local user profiles present on the system.
- Identifies which accounts have administrative privileges.
- Shows the filesystem location of each profile directory.
- Detects hidden or disabled accounts.
- Provides registry key modification times and ACL details.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `user_sid`   |
|Description    | `path`   |
|Additional Description    | `is_admin`   |
|    | `user_name`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `user_name` | String | USER_NAME | account name derived from the profile directory |
| `user_sid` | String | USER_SID | security identifier (SID) of the user profile |
| `path` | String | FILE_PATH | filesystem path to the user's profile directory |
| `is_hidden` | Bool |  | True if the account is listed as hidden in SpecialAccounts\UserList |
| `is_admin` | Bool |  | True if the profile's State flag indicates administrative rights (0x100 set) |
| `ref_count` | String |  | reference count value for the profile entry |
| `state` | String |  | raw State field value from the registry (used to infer admin status) |
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
