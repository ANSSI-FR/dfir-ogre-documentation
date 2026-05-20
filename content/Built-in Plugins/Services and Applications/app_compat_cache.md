---
 title: 'App Compat Cache'
---


{{< callout type="important" >}}Data Type: **app_compat_cache** \
	Python Parser: **RegAppCompatCache**{{< /callout >}}

### Description 

Extracts entries from the `AppCompatCache` value stored in the Windows `System` hive. It parses binary cache data, emitting each cached executable’s path, last‑write time, and associated registry metadata.

- Provides the original file path used by the system for compatibility checks.
- Shows when the cache entry was last updated, helping to infer program execution timelines.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `path`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `index` | Int |  | sequential index of the cache entry |
| `path` | String | FILE_PATH | file path of the cached executable |
| `modification_date` | DateTime | DATE_MODIFICATION | last write time of the cached executable |
| `flag1` | String |  | unknown 4‑byte flag data (Windows 8 AppCompatCache) |
| `flag2` | String |  | unknown 4‑byte flag data (Windows 8 AppCompatCache) |
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
