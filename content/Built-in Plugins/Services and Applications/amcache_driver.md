---
 title: 'Amcache Driver'
---


{{< callout type="important" >}}Data Type: **amcache_driver** \
	Python Parser: **RegAmCacheDriver**{{< /callout >}}

### Description 

Extracts driver metadata stored in the `AmCache` hive.

- Retrieves driver attributes (name, version, product, company, etc.).
- Captures file‑system information (path, size, SHA‑1, compilation date).


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
| `sha1` | String | FILE_SHA1 | Sha-1 signature |
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
