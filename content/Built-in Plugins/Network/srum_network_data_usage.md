---
 title: 'Srum Network Data Usage'
---


{{< callout type="important" >}}Data Type: **srum_network_data_usage** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

SRUM table that tracks how much network traffic each installed app consumes


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
