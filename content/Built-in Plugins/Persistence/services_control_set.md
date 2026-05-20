---
 title: 'Services Control Set'
---


{{< callout type="important" >}}Data Type: **services_control_set** \
	Python Parser: **RegServicesControlSet**{{< /callout >}}

### Description 

Extracts all service definitions from a Windows `System` hive, in the related control‑set keys.

- Provides service identifiers and display names.
- Shows how the service is configured (type, start type, image path).
- Reveals the account (user or system) that owns / runs the service.
- Supplies raw values useful for correlation with other artefacts.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `name`   |
|    | `display_name`   |
|Additional Description    | `service_type`   |
|    | `start_type`   |
|    | `image_path`   |
|    | `run_as`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `name` | String | SERVICE_NAME | unique identifier of the service (registry key name) |
| `service_type` | String | SERVICE_TYPE | type of the service (e.g., Kernel driver, WIN32 service, packaged service) |
| `display_name` | String | SERVICE_DISPLAY_NAME | human‑readable display name of the service |
| `description` | String |  | textual description of the service |
| `error_control` | String |  | error‑control setting (Ignore, Normal, Severe, Critical) |
| `service_type` | String | SERVICE_TYPE | type of the service (duplicate entry for compatibility) |
| `start_type` | String | SERVICE_START_TYPE | service start mode (Boot, System, Auto, Manual, Disabled) |
| `is_interactive` | Bool |  | whether the service is interactive |
| `is_packaged_service` | Bool |  | whether the service is a packaged (UWP) service |
| `is_service_driver` | Bool |  | whether the service is a driver (kernel, file‑system or recogniser) |
| `is_service_win32` | Bool |  | whether the service is a WIN32 service |
| `image_path` | String | COMMAND_LINE | command line or executable path that the service runs |
| `group` | String |  | load‑order group name the service belongs to |
| `tag` | String |  | numeric tag used for service ordering |
| `depend_on_group` | String |  | service groups this service depends on |
| `depend_on_service` | String | SERVICE_NAME | other services this service depends on |
| `delete_flag` | String |  | flag indicating the service is marked for deletion |
| `object_name` | String | WINDOWS_OBJECT | kernel object name for driver services |
| `run_as` | String | USER_NAME | account name under which the service runs |
| `wow64` | String |  | WOW64 flag indicating a 32‑bit service on a 64‑bit OS |
| `alias` | String | SERVICE_NAME | alternative name (alias) for the service |
| `delayed_auto_start` | String |  | whether the service uses delayed automatic start |
| `preshutdown_timeout` | String |  | pre‑shutdown timeout value (milliseconds) |
| `service_sid_type` | String |  | SID type assigned to the service (None, Unrestricted, Restricted) |
| `required_privileges` | String | WINDOWS_PRIVILEGES | list of privileges the service requires |
| `launch_protected` | String |  | protected‑process level of the service (None, Windows, Light, etc.) |
| `user_service_flags` | String |  | flags controlling user‑service permissions (e.g., DSMA allow) |
| `svchost_split_disable` | String |  | whether svchost split is disabled for this service |
| `package_fullname` | String |  | full package name for a packaged service |
| `app_usermodel_id` | String |  | AppUserModel ID associated with the service |
| `package_origin` | String |  | origin of the package (Unsigned, Inbox, Store, Developer) |
| `service_dll` | String | FILE_PATH | path to the ServiceDll implementing the service |
| `service_manifest` | String | FILE_PATH | path to the ServiceManifest file |
| `service_main` | String |  | name(s) of the service's main entry point function(s) |
| `parameters_key_last_modif` | DateTime | DATE_MODIFICATION | last modification timestamp of the Parameters sub‑key |
| `parameters_service_dll` | String | FILE_PATH | ServiceDll value inside the Parameters sub‑key |
| `parameters_service_manifest` | String | FILE_PATH | ServiceManifest value inside the Parameters sub‑key |
| `parameters_service_main` | String |  | ServiceMain value inside the Parameters sub‑key |
| `performance_key_last_modif` | DateTime | DATE_MODIFICATION | last modification timestamp of the Performance sub‑key |
| `performance_library` | String | FILE_PATH | library file used for performance counters |
| `performance_open_function` | String |  | function name that opens performance data |
| `performance_collect_function` | String |  | function name that collects performance data |
| `performance_close_function` | String |  | function name that closes performance data |
| `failure_actions` | String |  | binary blob describing service failure actions |
| `failure_command` | String | COMMAND_LINE | command executed when the service fails |
| `failure_actions_on_non_crash_failures` | Bool |  | whether failure actions apply to non‑crash failures |
| `key_path` | String | KEY_PATH |  full registry key name |
| `key_modif_time` | DateTime | DATE_MODIFICATION |  last modification timestamp of the registry key |
| `key_security` | Object |  |  |
| `key_security.owner_sid` | String | USER_SID |  SID of the user that owns the registry key |
| `key_security.group_sid` | String |  |  SID of the group that owns the registry key |
| `key_security.control_flags[]` | Array[String] |  |  security descriptor control flags for the key |
| `key_security.dacl_ace` | Object |  |  |
| `key_security.dacl_ace.ace_type` | String |  |  type of ACE (e.g., allow, deny) |
| `key_security.dacl_ace.account_sid` | String |  |  SID of the account the ACE applies to |
| `key_security.dacl_ace.ace_flags[]` | Array[String] |  |  ACE flags that modify inheritance or behavior |
| `key_security.dacl_ace.rights[]` | Array[String] |  |  permissions granted or denied by the ACE |
