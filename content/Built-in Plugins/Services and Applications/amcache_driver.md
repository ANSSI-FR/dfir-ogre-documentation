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

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `name` | String | FILE_NAME | file name |
| `path` | String | FILE_PATH | file path |
| `size` | Int | FILE_SIZE | file size |
| `inf` | String | FILE_NAME | name of the associated .inf file |
| `package_name` | String |  | name of the driver's package |
| `service` | String | SERVICE_NAME | name of the service installed by the driver |
| `version` | String | PE_VERSION | driver's version |
| `product` | String |  | name of the product |
| `product_version` | String | PE_VERSION | product's version |
| `company` | String | COMPANY | company providing the driver |
| `driver_type` | Int |  |  |
| `compilation_date` | DateTime | DATE_COMPILATION | compilation date |
| `image_size` | Int |  | equivalent to 'SizeOfImage' field of the PE header |
| `checksum` | Int |  | driver's checksum |
| `wdf_version` | String | PE_VERSION | Windows Driver Framework version |
| `driver_id` | String |  | raw Amcache driver identifier |
| `sha1` | String | FILE_SHA1 | normalized 40-hex SHA-1 hash of the driver |
| `key_path` | String | KEY_PATH | full registry key name |
| `key_modif_time` | DateTime | DATE_MODIFICATION | last modification timestamp of the registry key |
| `key_security` | Object |  |  |
| `key_security.owner_sid` | String | USER_SID | SID of the user that owns the registry key |
| `key_security.group_sid` | String |  | SID of the group that owns the registry key |
| `key_security.control_flags[]` | Array[String] |  | security descriptor control flags for the key |
| `key_security.sacl_aces[]` | Array[Object] |  |  |
| `key_security.sacl_aces[].ace_type` | String |  | type of ACE (e.g., allow, deny) |
| `key_security.sacl_aces[].ace_flags[]` | Array[String] |  | ACE flags that modify inheritance or behavior |
| `key_security.sacl_aces[].rights[]` | Array[String] |  | permissions granted or denied by the ACE |
| `key_security.sacl_aces[].account_sid` | String |  | SID of the account the ACE applies to |
| `key_security.sacl_aces[].ace_size` | Int |  | declared ACE size in bytes |
| `key_security.sacl_aces[].object_type_guid` | String |  | GUID identifying the object type governed by the ACE |
| `key_security.sacl_aces[].inherited_object_type_guid` | String |  | GUID identifying the inherited object type governed by the ACE |
| `key_security.sacl_aces[].raw_hex` | String |  | raw ACE bytes preserved as hexadecimal |
| `key_security.dacl_aces[]` | Array[Object] |  |  |
| `key_security.dacl_aces[].ace_type` | String |  | type of ACE (e.g., allow, deny) |
| `key_security.dacl_aces[].ace_flags[]` | Array[String] |  | ACE flags that modify inheritance or behavior |
| `key_security.dacl_aces[].rights[]` | Array[String] |  | permissions granted or denied by the ACE |
| `key_security.dacl_aces[].account_sid` | String |  | SID of the account the ACE applies to |
| `key_security.dacl_aces[].ace_size` | Int |  | declared ACE size in bytes |
| `key_security.dacl_aces[].object_type_guid` | String |  | GUID identifying the object type governed by the ACE |
| `key_security.dacl_aces[].inherited_object_type_guid` | String |  | GUID identifying the inherited object type governed by the ACE |
| `key_security.dacl_aces[].raw_hex` | String |  | raw ACE bytes preserved as hexadecimal |
