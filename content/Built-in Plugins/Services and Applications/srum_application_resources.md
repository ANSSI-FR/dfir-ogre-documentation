---
 title: 'Srum Application Resources'
---


{{< callout type="important" >}}Data Type: **srum_application_resources** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Srum table that tracks ressource usage for every exe that’s executed on the system
      whether it still exists on disk or not. If it executed, it should be logged.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `user_id`   |
|Description    | `app_id`   |
|Additional Description    | `face_time`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `incremental_id` | Int |  |  |
| `timestamp` | DateTime |  |  |
| `app_id` | String | APP_ID |  |
| `user_id` | String | USER_ID |  |
| `face_time` | Int |  |  |
| `foreground_cycle_time` | Int |  |  |
| `background_cycle_time` | Int |  |  |
| `foreground_context_switches` | Int |  |  |
| `background_context_switches` | Int |  |  |
| `foreground_bytes_read` | Int |  |  |
| `background_bytes_read` | Int |  |  |
| `foreground_bytes_written` | Int |  |  |
| `background_bytes_written` | Int |  |  |
| `foreground_num_read_operations` | Int |  |  |
| `background_num_read_operations` | Int |  |  |
| `foreground_num_write_operations` | Int |  |  |
| `background_num_write_operations` | Int |  |  |
| `foreground_number_of_flushes` | Int |  |  |
| `background_number_of_flushes` | Int |  |  |
