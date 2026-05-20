---
 title: 'Reg Keys'
---


{{< callout type="important" >}}Data Type: **reg_keys** \
	Python Parser: **HiveKey**{{< /callout >}}

### Description 

Extracts detailed information from Windows Registry hive files. It reads each key, its path, associated values, and security descriptors,

- Retrieves key names, full paths, and timestamps.
- Retrieves every assiociated values.
- Includes ownership information (owner SID) from key security descriptors.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `descriptor.owner_sid`   |
|Description    | `path`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `name` | String | KEY_NAME | registry key name |
| `path` | String | KEY_PATH | full registry key name |
| `mtime` | DateTime | DATE_MODIFICATION | last modification timestamp of the registry key |
| `values[]` | Array[Object] |  |  |
| `values[].name` | String | VALUE_NAME | value name |
| `values[].data` | String |  | data stored in the value |
| `values[].type` | String |  | type of the registry value (e.g., REG_SZ, REG_DWORD) |
| `values[].size` | Int |  | size of the value data in bytes |
| `values[].error` | String |  | error message if the value could not be parsed |
| `descriptor` | Object |  |  |
| `descriptor.owner_sid` | String | USER_SID | SID of the user that owns the registry key |
| `descriptor.group_sid` | String |  | SID of the group that owns the registry key |
| `descriptor.control_flags[]` | Array[String] |  | security descriptor control flags for the key |
| `descriptor.dacl_ace` | Object |  |  |
| `descriptor.dacl_ace.ace_type` | String |  | type of ACE (e.g., allow, deny) |
| `descriptor.dacl_ace.account_sid` | String |  | SID of the account the ACE applies to |
| `descriptor.dacl_ace.ace_flags[]` | Array[String] |  | ACE flags that modify inheritance or behavior |
| `descriptor.dacl_ace.rights[]` | Array[String] |  | permissions granted or denied by the ACE |
