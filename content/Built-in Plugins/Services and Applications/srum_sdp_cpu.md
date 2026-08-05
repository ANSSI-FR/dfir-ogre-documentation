---
 title: 'Srum Sdp Cpu'
---


{{< callout type="important" >}}Data Type: **srum_sdp_cpu** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Each row is Windows Server SRUM SDP processor telemetry with timestamp and accumulated processor time plus application and user identifiers where recorded. Use it to compare CPU usage context across intervals. The counter is aggregate telemetry and does not reveal individual instructions, threads, or actions.


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
| `processor_time` | Int |  |
