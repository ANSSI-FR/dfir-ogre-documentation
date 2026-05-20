---
 title: 'Srum Sdp Volume'
---


{{< callout type="important" >}}Data Type: **srum_sdp_volume** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Srum table for windows server 2022 that tracks storage volumes information


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
| `total` | Int |  |  |
| `used` | Int |  |  |
