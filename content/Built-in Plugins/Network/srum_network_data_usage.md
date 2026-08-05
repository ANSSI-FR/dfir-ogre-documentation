---
 title: 'Srum Network Data Usage'
---


{{< callout type="important" >}}Data Type: **srum_network_data_usage** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Each row is an SRUM network-usage interval associated with an application, user, interface, and profile, with bytes sent and received. Use it to identify applications with network activity and correlate volume changes with other events. It provides aggregate byte counts, not remote endpoints, protocols, payloads, or individual connections.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `user_id`   |
|Description    | `app_id`   |
|Additional Description    | `bytes_sent`   |
|    | `bytes_recvd`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `incremental_id` | Int |  |  |
| `timestamp` | DateTime |  |  |
| `app_id` | String | APP_ID |  |
| `user_id` | String | USER_ID |  |
| `interface_luid` | Int |  |  |
| `l2_profile_id` | Int |  |  |
| `l2_profile_flags` | Int |  |  |
| `bytes_sent` | Int |  |  |
| `bytes_recvd` | Int |  |  |
