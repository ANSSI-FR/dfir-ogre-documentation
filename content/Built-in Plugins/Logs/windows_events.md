---
 title: 'Windows Events'
---


{{< callout type="important" >}}Data Type: **windows_events** \
	Python Parser: **Evtx**{{< /callout >}}

### Description 

Parses windows evtx logs.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `system.security.user_id`   |
|Description    | `system.provider.provider_name`   |
|    | `system.event_id`   |
|Additional Description    | `event_data.device_instance_id`   |
|    | `event_data.driver_name`   |
|    | `user_data.event_processing_failure.publisher_id`   |
|    | `user_data.event_processing_failure.error_code`   |
|    | `user_data.event_processing_failure.event_id`   |
|    | `event_data.pua_policy_id`   |
|    | `event_data.param1`   |
|    | `event_data.param2`   |
|    | `event_data`   |
|    | `user_data`   |
|    | `debug_data`   |
|    | `processing_error_data`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `timestamp` | DateTime | DATE_CREATION | timestamp of when the event was generated |
| `system` | Object |  |  |
| `system.security` | Object |  |  |
| `system.security.user_id` | String | USER_ID | SID of the account that generated the event |
| `system.time_created` | Object |  |  |
| `system.time_created.system_time` | DateTime | DATE_CREATION | system time recorded for the event |
| `system.provider` | Object |  |  |
| `system.provider.provider_name` | String |  | name of the event provider |
| `system.provider.guid` | String |  | GUID of the event provider |
| `system.execution` | Object |  |  |
| `system.execution.process_id` | String |  | process identifier that generated the event |
| `system.execution.thread_id` | String |  | thread identifier that generated the event |
| `system.event_record_id` | String |  | unique record identifier for the event |
| `system.computer` | String |  | name of the computer that logged the event |
| `system.event_id` | String |  | numeric identifier of the event type |
| `event_data` | Object |  |  |
| `user_data` | Object |  |  |
| `debug_data` | Object |  |  |
| `binary_event_data` | Object |  |  |
| `processing_error_data` | Object |  |  |
| `rendering_info` | Object |  |  |
