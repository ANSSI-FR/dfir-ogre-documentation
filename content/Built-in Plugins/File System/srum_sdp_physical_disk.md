---
 title: 'Srum Sdp Physical Disk'
---


{{< callout type="important" >}}Data Type: **srum_sdp_physical_disk** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Each row is Windows Server SRUM SDP physical-disk telemetry with timestamp and disk-size value plus application and user identifiers where recorded. Use it to establish storage-resource context across observations. The mapping exposes aggregate size only and cannot identify partitions, files, or individual disk operations.


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
| `size_in_bytes` | Int |  |
