---
 title: 'Reg Systeminfo'
---


{{< callout type="important" >}}Data Type: **reg_systeminfo** \
	Python Parser: **RegSystemInfo**{{< /callout >}}

### Description 

Extracts various system information from the SYSTEM and SOFTWARE hives


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `product_name`   |
|Additional Description    | `os_version`   |
|    | `build_number`   |
|    | `architecture`   |
|    | `timezone_iana`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `computer_name` | String |  | Name of the computer |
| `product_name` | String |  | Windows product name (e.g., Windows 10 Pro) |
| `os_version` | String |  | Windows version number (major.minor |
| `build_number` | String |  | Windows build number |
| `install_date` | DateTime |  | UTC timestamp when Windows was installed |
| `shutdown_date` | DateTime |  | Last recorded shutdown time in UTC |
| `domain` | String |  | Domain the computer is joined to (if any) |
| `system_root` | String |  | Windows system directory path (typically C:\Windows) |
| `architecture` | String |  | Processor architecture (e.g., AMD64, x86) |
| `has_emet` | Bool |  | True if EMET (Enhanced Mitigation Experience Toolkit) is installed |
| `is_dc` | Bool |  | True if this computer is a Domain Controller |
| `is_pki` | Bool |  | True if this computer has the PKI role |
| `is_ias` | Bool |  | True if this computer has the IAS role |
| `app_whitelisting` | String |  | Application whitelisting policy in use (AppLocker, SRP, or empty) |
| `timezone_windows` | String |  | Windows timezone key name from registry |
| `timezone_iana` | String |  | IANA timezone identifier converted from Windows timezone |
| `wu_last_check` | DateTime |  | Last successful Windows Update detection scan time |
| `wu_last_download` | DateTime |  | Last successful Windows Update download time |
| `wu_last_install` | DateTime |  | Last successful Windows Update installation time |
| `install_date_local` | String |  | Local timezone timestamp when Windows was installed |
| `control_set` | String |  | Active ControlSet currently in use (ControlSet001, ControlSet002, etc.) |
| `interfaces[]` | Array[Object] |  |  |
| `interfaces[].guid` | String |  | Unique identifier for the network interface |
| `interfaces[].name` | String |  | Network interface name as shown in Windows |
| `interfaces[].description` | String |  | Network interface description |
| `interfaces[].mac` | String |  | Physical MAC address of the interface |
| `interfaces[].ipv4` | String |  | IPv4 addresses assigned to the interface |
| `interfaces[].dhcp_enabled` | String |  | Whether DHCP is enabled for this interfac |
| `interfaces[].dhcp_ipv4` | String |  | Current IPv4 address obtained via DHCP |
| `interfaces[].dhcp_ipv4_server` | String |  | DHCP server that provided the IPv4 address |
| `interfaces[].ipv6` | String |  | IPv6 addresses assigned to the interface |
| `interfaces[].dhcp_ipv6` | String |  | Current IPv6 address obtained via DHCP |
| `interfaces[].dhcp_ipv6_server` | String |  | DHCP server that provided the IPv6 address |
