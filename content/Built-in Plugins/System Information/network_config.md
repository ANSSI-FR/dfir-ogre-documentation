---
 title: 'Network Config'
---


{{< callout type="important" >}}Data Type: **network_config** \
	Python Parser: **RegNetworkConfig**{{< /callout >}}

### Description 

Extracts network settings from the Windows `System` hive.

- Shows static IP assignments when DHCP is disabled.
- Provides DHCP‑derived addresses and DNS when enabled.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `ip_address`   |
|    | `dns_suffix`   |
|    | `dhcp`   |
|Additional Description    | `network_mask`   |
|    | `gateway`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `ip_address` | String | IP_ADDRESS | IP address assigned to the network interface |
| `network_mask` | String |  | Subnet mask associated with the IP address |
| `dhcp` | Bool |  |  |
| `dhcp_server` | String |  | Address of the DHCP server that provided the configuration |
| `dns_suffix` | String |  | DNS suffix (domain) applied to the interface |
| `name_servers` | String |  | Comma‑separated list of DNS name‑server addresses |
| `gateway` | String |  | Default gateway IP address for the interface |
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
