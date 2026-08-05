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
| `path` | String |  |
| `mtime` | DateTime |  |
| `security_descriptor` | Object |  |
| `security_descriptor.owner_sid` | String |  |
| `security_descriptor.group_sid` | String |  |
| `security_descriptor.control_flags[]` | Array[String] |  |
| `security_descriptor.sacl_aces[]` | Array[Object] |  |
| `security_descriptor.sacl_aces[].ace_type` | String |  |
| `security_descriptor.sacl_aces[].ace_flags[]` | Array[String] |  |
| `security_descriptor.sacl_aces[].rights[]` | Array[String] |  |
| `security_descriptor.sacl_aces[].account_sid` | String |  |
| `security_descriptor.sacl_aces[].ace_size` | Int |  |
| `security_descriptor.sacl_aces[].object_type_guid` | String |  |
| `security_descriptor.sacl_aces[].inherited_object_type_guid` | String |  |
| `security_descriptor.sacl_aces[].raw_hex` | String |  |
| `security_descriptor.dacl_aces[]` | Array[Object] |  |
| `security_descriptor.dacl_aces[].ace_type` | String |  |
| `security_descriptor.dacl_aces[].ace_flags[]` | Array[String] |  |
| `security_descriptor.dacl_aces[].rights[]` | Array[String] |  |
| `security_descriptor.dacl_aces[].account_sid` | String |  |
| `security_descriptor.dacl_aces[].ace_size` | Int |  |
| `security_descriptor.dacl_aces[].object_type_guid` | String |  |
| `security_descriptor.dacl_aces[].inherited_object_type_guid` | String |  |
| `security_descriptor.dacl_aces[].raw_hex` | String |  |
| `name` | String |  |
| `data` | String |  |
| `type` | String |  |
| `size` | Int |  |
| `is_placeholder` | Bool |  |
| `invalid_signature` | Bool |  |
| `error` | String |  |
