---
 title: 'Recent App'
---


{{< callout type="important" >}}Data Type: **recent_app** \
	Python Parser: **RegRecentApp**{{< /callout >}}

### Description 

Each row describes an application or recent item from the short-lived Windows 10 RecentApps artifact, with program identity, launch count, last access time, file path, and arguments where available. Use it to associate applications with recently accessed files. The artifact is limited to Windows 10 versions 1607 through 1709, has finite retention, and absence does not exclude use.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `path`   |
|Additional Description    | `launch_count`   |
|    | `display_name`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `guid_app` | String | GUID of the application |
| `app_id` | String | Application identifier |
| `app_path` | String | Path of the application executable |
| `launch_count` | Int | Number of times the application has been launched |
| `app_last_accessed_time` | DateTime | Timestamp of the last time the application was accessed |
| `guid_file` | String | GUID of the recently accessed file |
| `display_name` | String | Human‑readable display name of the recent file |
| `path` | String | Path of the recently accessed item |
| `arguments` | String | Optional arguments associated with the recently accessed item |
| `file_last_accessed_time` | DateTime | Timestamp of the last time the file was accessed |
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
