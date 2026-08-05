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
| `incremental_id` | Int | Auto-increment identifier of the SRUM record |
| `timestamp` | DateTime | Timestamp of the SRUM record |
| `app_id` | String | Identifier of the application |
| `user_id` | String | Identifier (SID) of the user |
| `total` | Int |  |
| `used` | Int |  |
