---
 title: 'Srum Network Connectivity Usage'
---


{{< callout type="important" >}}Data Type: **srum_network_connectivity_usage** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Each row is an SRUM network-connectivity interval associated with an application, user, interface, and layer-2 profile, with connection start time and duration. Use it to place application network availability on a timeline and correlate profiles or interfaces. It records connectivity duration, not remote endpoints, payloads, or proof of a specific communication.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `user_id`   |
|Description    | `app_id`   |
|    | `interface_luid`   |
|Additional Description    | `connected_time`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `incremental_id` | Int |  |
| `timestamp` | DateTime |  |
| `app_id` | String |  |
| `user_id` | String |  |
| `interface_luid` | Int |  |
| `connect_start_time` | DateTime |  |
| `connected_time` | Int |  |
| `l2_profile_id` | Int |  |
| `l2_profile_flags` | Int |  |
