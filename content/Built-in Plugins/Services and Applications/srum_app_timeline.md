---
 title: 'Srum App Timeline'
---


{{< callout type="important" >}}Data Type: **srum_app_timeline** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Srum table that tracks statistics about inputs (focus, keyboard, mouse, etc.)
      recieved by each application


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `user_id`   |
|Description    | `app_id`   |
|Additional Description    | `in_focus_s`   |
|    | `duration_ms`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `incremental_id` | Int |  |  |
| `timestamp` | DateTime |  |  |
| `app_id` | String | APP_ID |  |
| `user_id` | String | USER_ID |  |
| `flags` | Int |  |  |
| `in_focus_s` | Int |  |  |
| `duration_ms` | Int |  |  |
| `span_ms` | Int |  |  |
| `user_input_s` | Int |  |  |
| `keyboard_input_s` | Int |  |  |
| `mouse_input_s` | Int |  |  |
| `audio_in_s` | Int |  |  |
| `audio_out_s` | Int |  |  |
| `disk_raw` | Int |  |  |
| `network_tail_raw` | Int |  |  |
| `network_bytes_raw` | Int |  |  |
| `pms_foreground_s` | Int |  |  |
| `comp_rendered_s` | Int |  |  |
| `comp_dirtied_s` | Int |  |  |
| `comp_propagated_s` | Int |  |  |
| `cycles` | Int |  |  |
| `cycles_breakdown` | Int |  |  |
| `cycles_attr` | Int |  |  |
| `cycles_attr_breakdown` | Int |  |  |
| `cycles_wob` | Int |  |  |
| `cycles_wob_breakdown` | Int |  |  |
| `disk_raw` | Int |  |  |
| `network_tail_raw` | Int |  |  |
| `network_bytes_raw` | Int |  |  |
| `mbb_tail_raw` | Int |  |  |
| `mbb_bytes_raw` | Int |  |  |
| `display_required_s` | Int |  |  |
| `end_time` | Int |  |  |
| `timeline_end` | Int |  |  |
| `display_required_timeline` | Int |  |  |
| `keyboard_input_timeline` | Int |  |  |
| `user_input_timeline` | Int |  |  |
| `comp_rendered_timeline` | Int |  |  |
| `comp_dirtied_timeline` | Int |  |  |
| `comp_propagated_timeline` | Int |  |  |
| `audio_in_timeline` | Int |  |  |
| `audio_out_timeline` | Int |  |  |
| `cpu_timeline` | Int |  |  |
| `disk_timeline` | Int |  |  |
| `network_timeline` | Int |  |  |
| `mbb_timeline` | Int |  |  |
