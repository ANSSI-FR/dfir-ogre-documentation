---
 title: 'Amcache Program'
---


{{< callout type="important" >}}Data Type: **amcache_program** \
	Python Parser: **RegAmCacheProgram**{{< /callout >}}

### Description 

Extracts metadata about installed programs from the Windows `AmCache` hive.

- Retrieves program identifiers, names, versions, and publishers.
- Captures installation source, directory paths, and MSI product/package codes.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `name`   |
|Additional Description    | `version`   |
|    | `publisher`   |
|    | `install_dir`   |
|    | `key_path`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `id` | String | APP_ID | Program identifier |
| `name` | String | APP_NAME | Program name |
| `version` | String | PE_VERSION | Program version |
| `publisher` | String | PUBLISHER | Program publisher |
| `source` | String |  | Installation method ('MSI', 'AppxPackage', 'AddRemoveProgram') |
| `install_date` | DateTime | DATE_INSTALLATION | Installation date, present if the program is installed via MSI, the time is always 00:00:00 |
| `uninstall_date` | DateTime | DATE_UNINSTALL | Uninstall date |
| `msi_product_code` | String | MSI_PRODUCT | Product code, present if the program is installed via MSI |
| `msi_package_code` | String | MSI_PACKAGE | Package code, present if the program is installed via MSI  |
| `instance_id` | String |  | Equivalent of the 'ProgramInstanceId', hash of the file identifier |
| `inbox_modern_app` | Bool |  |  |
| `os_at_install` | String | OS_VERSION | 4 bytes of the operating‑system version during program installation. |
| `install_dir` | String | FILE_PATH | Path of the program installation directory. |
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
