---
 title: 'Recent App'
---


{{< callout type="important" >}}Data Type: **recent_app** \
	Python Parser: **RegRecentApp**{{< /callout >}}

### Description 

Extracts information about applications and files recently accessed by a user from the `NtUser` hive. It parses each RecentApps key and its `RecentItems` sub‑key.

- Provides per-application identifiers and launch statistics.
- Captures timestamps of the last access for both the application and individual files.
- Includes the full command line (path+arguments) used to launch each recent file.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `path`   |
|Additional Description    | `launch_count`   |
|    | `display_name`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `guid_app` | String |  | GUID of the application |
| `app_id` | String | APP_ID | Application identifier |
| `launch_count` | Int |  | Number of times the application has been launched |
| `app_last_accessed_time` | DateTime | DATE_ACCESS | Timestamp of the last time the application was accessed |
| `guid_file` | String |  | GUID of the recently accessed file |
| `display_name` | String |  | Human‑readable display name of the recent file |
| `path` | String |  | Full command line (file path plus arguments) used to launch the file |
| `file_last_accessed_time` | DateTime | DATE_ACCESS | Timestamp of the last time the file was accessed |
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
