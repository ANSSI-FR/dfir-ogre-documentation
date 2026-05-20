---
 title: 'Srum Network Connectivity Usage'
---


{{< callout type="important" >}}Data Type: **srum_network_connectivity_usage** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Srum table that tracks network connection time statistics per interface


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `user_id`   |
|Description    | `app_id`   |
|    | `interface_luid`   |
|Additional Description    | `connected_time`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `incremental_id` | Int |  |  |
| `timestamp` | DateTime |  |  |
| `app_id` | String | APP_ID |  |
| `user_id` | String | USER_ID |  |
| `interface_luid` | Int |  |  |
| `connect_start_time` | DateTime |  |  |
| `connected_time` | Int |  |  |
| `l2_profile_id` | Int |  |  |
| `l2_profile_flags` | Int |  |  |
