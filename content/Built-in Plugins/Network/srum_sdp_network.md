---
 title: 'Srum Sdp Network'
---


{{< callout type="important" >}}Data Type: **srum_sdp_network** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Each row is Windows Server SRUM SDP network telemetry with timestamp and inbound, outbound, and total byte counters plus application and user identifiers where recorded. Use it to identify changes in aggregate network use. The counters do not expose endpoints, protocols, payloads, or individual connections.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `user_id`   |
|Description    | `app_id`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `incremental_id` | Int |  |  |
| `timestamp` | DateTime |  |  |
| `app_id` | String | APP_ID |  |
| `user_id` | String | USER_ID |  |
| `bytes_in_bound` | Int |  |  |
| `bytes_out_bound` | Int |  |  |
| `bytes_total` | Int |  |  |
