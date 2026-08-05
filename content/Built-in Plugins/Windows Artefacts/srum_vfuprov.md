---
 title: 'Srum Vfuprov'
---


{{< callout type="important" >}}Data Type: **srum_vfuprov** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Each row preserves an SRUM VFU provider table record with timestamp, application identifier, user identifier, and database identity fields. Use these keys to correlate otherwise opaque provider records with other SRUM tables. Because no provider-specific payload is decoded, interpretation should remain limited to presence and temporal association.


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
