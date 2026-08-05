---
 title: 'Amcache Driver'
---


{{< callout type="important" >}}Data Type: **amcache_driver** \
	Python Parser: **RegAmCacheDriver**{{< /callout >}}

### Description 

Each row is a driver inventory record from the Amcache hive, with driver name and path, identifier or hash, version, vendor, size, and compilation metadata. Use it to identify rare or vulnerable drivers and correlate binaries across hosts. Amcache inventory presence does not establish that the driver loaded or executed, and fields vary by Windows version.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `name`   |
|Additional Description    | `path`   |
|    | `size`   |
|    | `service`   |
|    | `key_path`   |
|    | `sha1`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `name` | String | Driver file name |
| `path` | String | Driver file path on disk |
| `size` | Int | Driver file size in bytes |
| `inf` | String | name of the associated .inf file |
| `package_name` | String | name of the driver's package |
| `service` | String | name of the service installed by the driver |
| `version` | String | Driver version |
| `product` | String | name of the product |
| `product_version` | String | Product version |
| `company` | String | company providing the driver |
| `driver_type` | Int | Driver load type (e.g., boot, kernel, filter) |
| `compilation_date` | DateTime | Driver compilation date |
| `image_size` | Int | equivalent to 'SizeOfImage' field of the PE header |
| `checksum` | Int | Driver image checksum |
| `wdf_version` | String | Windows Driver Framework version |
| `driver_id` | String | raw Amcache driver identifier |
| `sha1` | String | normalized 40-hex SHA-1 hash of the driver |
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
