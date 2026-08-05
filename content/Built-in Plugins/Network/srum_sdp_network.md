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

| Output Name | Data Type | Description |
|---|---|---|
| `incremental_id` | Int | Auto-increment identifier of the SRUM record |
| `timestamp` | DateTime | Timestamp of the SRUM record |
| `app_id` | String | Identifier of the application |
| `user_id` | String | Identifier (SID) of the user |
| `bytes_in_bound` | Int |  |
| `bytes_out_bound` | Int |  |
| `bytes_total` | Int |  |
