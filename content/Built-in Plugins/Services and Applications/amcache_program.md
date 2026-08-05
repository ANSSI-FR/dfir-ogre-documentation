---
 title: 'Amcache Program'
---


{{< callout type="important" >}}Data Type: **amcache_program** \
	Python Parser: **RegAmCacheProgram**{{< /callout >}}

### Description 

Each row is a program inventory record from the Amcache hive, with program identity, name, version, publisher, install source or path, and MSI identifiers where available. Use it to correlate installed software with related file records and enterprise inventory. Presence does not by itself prove installation time, current installation, or execution.


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

| Output Name | Data Type | Description |
|---|---|---|
| `id` | String | Program identifier |
| `name` | String | Program name |
| `version` | String | Program version |
| `publisher` | String | Program publisher |
| `source` | String | Installation method ('MSI', 'AppxPackage', 'AddRemoveProgram') |
| `install_date` | DateTime | Installation date, present if the program is installed via MSI, the time is always 00:00:00 |
| `uninstall_date` | DateTime | Date the program was uninstalled |
| `msi_product_code` | String | Product code, present if the program is installed via MSI |
| `msi_package_code` | String | Package code, present if the program is installed via MSI  |
| `instance_id` | String | Equivalent of the 'ProgramInstanceId', hash of the file identifier |
| `inbox_modern_app` | Bool | Whether the program is an inbox modern (UWP) app |
| `os_at_install` | String | 4 bytes of the operating‑system version during program installation. |
| `install_dir` | String | Path of the program installation directory. |
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
