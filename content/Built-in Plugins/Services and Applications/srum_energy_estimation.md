---
 title: 'Srum Energy Estimation'
---


{{< callout type="important" >}}Data Type: **srum_energy_estimation** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Each row preserves an SRUM energy-estimation record with timestamp, application and user identifiers, and an opaque binary payload. Use the identifiers and time for correlation or future schema-aware decoding. Because the payload is not interpreted by this mapping, it should not support claims about specific energy components or quantities.


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
| `binary_data` | String |  |
