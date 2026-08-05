---
 title: 'Srum Sdp Volume'
---


{{< callout type="important" >}}Data Type: **srum_sdp_volume** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Each row is Windows Server SRUM SDP volume telemetry with timestamp and total or used storage values plus application and user identifiers where recorded. Use it to track aggregate capacity changes or correlate resource context. It is summary telemetry, not evidence of which files caused the change.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `user_id`   |
|Description    | `app_id`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `incremental_id` | Int |  |
| `timestamp` | DateTime |  |
| `app_id` | String |  |
| `user_id` | String |  |
| `total` | Int |  |
| `used` | Int |  |
