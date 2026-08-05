---
 title: 'Srum Application Resources'
---


{{< callout type="important" >}}Data Type: **srum_application_resources** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Each row is a Windows SRUM resource-usage interval for an application and user, with foreground or background CPU cycles, context switches, and read, write, or flush counts. Use it to identify resource-intensive or previously observed applications and correlate usage over time. Aggregated counters do not reveal individual operations, and absence does not prove non-execution.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `user_id`   |
|Description    | `app_id`   |
|Additional Description    | `face_time`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `incremental_id` | Int | Auto-increment identifier of the SRUM record |
| `timestamp` | DateTime | Timestamp of the SRUM record |
| `app_id` | String | Identifier of the application |
| `user_id` | String | Identifier (SID) of the user |
| `face_time` | Int |  |
| `foreground_cycle_time` | Int |  |
| `background_cycle_time` | Int |  |
| `foreground_context_switches` | Int |  |
| `background_context_switches` | Int |  |
| `foreground_bytes_read` | Int |  |
| `background_bytes_read` | Int |  |
| `foreground_bytes_written` | Int |  |
| `background_bytes_written` | Int |  |
| `foreground_num_read_operations` | Int |  |
| `background_num_read_operations` | Int |  |
| `foreground_num_write_operations` | Int |  |
| `background_num_write_operations` | Int |  |
| `foreground_number_of_flushes` | Int |  |
| `background_number_of_flushes` | Int |  |
