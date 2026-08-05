---
 title: 'Network Configuration'
---


{{< callout type="important" >}}Data Type: **network_config** \
	Python Parser: **RegNetworkConfig**{{< /callout >}}

### Description 

Each row describes a Windows network-interface configuration from the SYSTEM hive, including interface identity, IP address, mask, gateway, DHCP and DNS values, plus registry provenance. Use it to establish host network context and correlate addresses with logs or captures. Settings can be historical, stale, or lease-derived and do not represent network traffic.


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

| Output Name | Data Type | Description |
|---|---|---|
| `ip_address` | String | IP address assigned to the network interface |
| `network_mask` | String | Subnet mask associated with the IP address |
| `dhcp` | Bool | Indicates whether the interface obtains its configuration via DHCP (true = DHCP enabled) |
| `dhcp_server` | String | Address of the DHCP server that provided the configuration |
| `dns_suffix` | String | DNS suffix (domain) applied to the interface |
| `name_servers` | String | Comma‑separated list of DNS name‑server addresses |
| `gateway` | String | Default gateway IP address for the interface |
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
