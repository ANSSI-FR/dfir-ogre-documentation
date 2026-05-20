---
 title: 'Srum Wpn Provider'
---


{{< callout type="important" >}}Data Type: **srum_wpn_provider** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Srum table that tracks telemetry that Windows collects about the Windows Push
      Notification (WPN) service – i.e., the background “push‑notification” system that delivers
      toast, badge, tile, and raw notifications to modern (UWP/Store) apps.


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
| `notification_type` | Int |  |  |
| `payload_size` | Int |  |  |
| `network_type` | Int |  |  |
