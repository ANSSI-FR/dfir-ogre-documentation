---
 title: 'Srum Tagged Energy'
---


{{< callout type="important" >}}Data Type: **srum_tagged_energy** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Each row preserves an SRUM tagged-energy table record with timestamp, application identifier, user identifier, and database identity fields. Use these keys to correlate otherwise opaque records with other SRUM tables. This mapping does not decode energy metrics, so the row should not support claims about consumption or activity type.


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
