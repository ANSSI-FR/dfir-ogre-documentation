---
 title: 'Hive'
---


{{< callout type="important" >}}Data Type: **hive** \
	Python Parser: **HiveKey**{{< /callout >}}

### Description 

Each row exposes a raw Windows Registry value with hive and key path, value name, type, data, key LastWrite time, security metadata, and parse errors where present. Use it for low-level configuration and provenance analysis when no specialized mapping applies. LastWrite is key-level, not a timestamp for each individual value.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `security_descriptor.owner_sid`   |
|Description    | `path`   |
|    | `name`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `path` | String | Full path of the registry key |
| `mtime` | DateTime | Last write (modification) time of the registry key |
| `security_descriptor` | Object |  |
| `security_descriptor.owner_sid` | String | SID of the key owner |
| `security_descriptor.group_sid` | String | SID of the primary group of the key |
| `security_descriptor.control_flags[]` | Array[String] | Security descriptor control flags (e.g., SE_DACL_PRESENT) |
| `security_descriptor.sacl_aces[]` | Array[Object] |  |
| `security_descriptor.sacl_aces[].ace_type` | String | Type of ACE (e.g., ACCESS_ALLOWED, ACCESS_DENIED) |
| `security_descriptor.sacl_aces[].ace_flags[]` | Array[String] | ACE flags that modify inheritance or behavior |
| `security_descriptor.sacl_aces[].rights[]` | Array[String] | Access rights granted or denied by the ACE |
| `security_descriptor.sacl_aces[].account_sid` | String | SID of the account the ACE applies to |
| `security_descriptor.sacl_aces[].ace_size` | Int | Size of the ACE structure in bytes |
| `security_descriptor.sacl_aces[].object_type_guid` | String | GUID identifying the ACE object type |
| `security_descriptor.sacl_aces[].inherited_object_type_guid` | String | GUID identifying the inherited object type |
| `security_descriptor.sacl_aces[].raw_hex` | String | Raw ACE bytes as hexadecimal |
| `security_descriptor.dacl_aces[]` | Array[Object] |  |
| `security_descriptor.dacl_aces[].ace_type` | String | Type of ACE (e.g., ACCESS_ALLOWED, ACCESS_DENIED) |
| `security_descriptor.dacl_aces[].ace_flags[]` | Array[String] | ACE flags that modify inheritance or behavior |
| `security_descriptor.dacl_aces[].rights[]` | Array[String] | Access rights granted or denied by the ACE |
| `security_descriptor.dacl_aces[].account_sid` | String | SID of the account the ACE applies to |
| `security_descriptor.dacl_aces[].ace_size` | Int | Size of the ACE structure in bytes |
| `security_descriptor.dacl_aces[].object_type_guid` | String | GUID identifying the ACE object type |
| `security_descriptor.dacl_aces[].inherited_object_type_guid` | String | GUID identifying the inherited object type |
| `security_descriptor.dacl_aces[].raw_hex` | String | Raw ACE bytes as hexadecimal |
| `name` | String | Name of the registry value |
| `data` | String | Data stored in the registry value |
| `type` | String | Registry value type (REG_*) |
| `size` | Int | Size of the value data in bytes |
| `is_placeholder` | Bool | Whether the value is a placeholder |
| `invalid_signature` | Bool | Whether the value has an invalid signature |
| `error` | String | Parse error message, if any |
