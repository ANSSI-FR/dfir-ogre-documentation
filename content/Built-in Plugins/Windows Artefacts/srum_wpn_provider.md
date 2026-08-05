---
 title: 'Srum Wpn Provider'
---


{{< callout type="important" >}}Data Type: **srum_wpn_provider** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Each row is Windows Push Notification telemetry from SRUM, associated with an application and user and including notification type, payload size, network type, and timestamp. Use it to correlate application notification activity with network and user timelines. It records notification metadata, not payload content or proof that a user viewed or acted on the notification.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `user_id`   |
|Description    | `app_id`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `incremental_id` | Int | Auto-increment identifier of the SRUM record |
| `timestamp` | DateTime | Timestamp of the SRUM record |
| `app_id` | String | Identifier of the application |
| `user_id` | String | Identifier (SID) of the user |
| `notification_type` | Int |  |
| `payload_size` | Int |  |
| `network_type` | Int |  |
