---
 title: 'Srum App Timeline'
---


{{< callout type="important" >}}Data Type: **srum_app_timeline** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Each row is a Windows SRUM application-timeline interval associated with an application and user, with focus duration, input, audio, network, disk, and CPU activity counters. Use it to compare application engagement and correlate resource activity over time. Counters are aggregated telemetry rather than individual actions, and coverage depends on SRUM retention.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `user_id`   |
|Description    | `app_id`   |
|Additional Description    | `in_focus_s`   |
|    | `duration_ms`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `incremental_id` | Int | Auto-increment identifier of the SRUM record |
| `timestamp` | DateTime | Timestamp of the SRUM record |
| `app_id` | String | Identifier of the application |
| `user_id` | String | Identifier (SID) of the user |
| `flags` | Int | Flags associated with the usage record |
| `in_focus_s` | Int | Time the app spent as the in-focus (foreground) window, in seconds |
| `duration_ms` | Int | Duration of the usage interval in milliseconds |
| `span_ms` | Int | Time span covered by the interval in milliseconds |
| `user_input_s` | Int | Time of user input activity, in seconds |
| `keyboard_input_s` | Int | Time of keyboard input activity, in seconds |
| `mouse_input_s` | Int | Time of mouse input activity, in seconds |
| `audio_in_s` | Int | Time performing audio input, in seconds |
| `audio_out_s` | Int | Time performing audio output, in seconds |
| `disk_raw` | Int | Raw disk usage count |
| `network_tail_raw` | Int | Raw network tail metric |
| `network_bytes_raw` | Int | Raw network bytes metric |
| `pms_foreground_s` | Int | Time the process spent in foreground (Process State Manager), in seconds |
| `comp_rendered_s` | Int | Time composing rendered content, in seconds |
| `comp_dirtied_s` | Int | Time composing dirtied content, in seconds |
| `comp_propagated_s` | Int | Time composing propagated content, in seconds |
| `cycles` | Int | Total CPU cycles used |
| `cycles_breakdown` | Int | CPU cycle usage breakdown |
| `cycles_attr` | Int | CPU cycles attributed to the process |
| `cycles_attr_breakdown` | Int | Breakdown of attributed CPU cycles |
| `cycles_wob` | Int | CPU cycles used without over-budget accounting |
| `cycles_wob_breakdown` | Int | Breakdown of non-over-budget CPU cycles |
| `disk_raw` | Int | Raw disk usage count |
| `network_tail_raw` | Int | Raw network tail metric |
| `network_bytes_raw` | Int | Raw network bytes metric |
| `mbb_tail_raw` | Int | Raw mobile broadband tail metric |
| `mbb_bytes_raw` | Int | Raw mobile broadband bytes metric |
| `display_required_s` | Int | Time the display was required to stay on, in seconds |
| `end_time` | Int | End time of the usage interval |
| `timeline_end` | Int | End of the usage timeline data |
| `display_required_timeline` | Int | Display-required timeline data |
| `keyboard_input_timeline` | Int | Keyboard input timeline data |
| `user_input_timeline` | Int | User input timeline data |
| `comp_rendered_timeline` | Int | Composition rendered timeline data |
| `comp_dirtied_timeline` | Int | Composition dirtied timeline data |
| `comp_propagated_timeline` | Int | Composition propagated timeline data |
| `audio_in_timeline` | Int | Audio input timeline data |
| `audio_out_timeline` | Int | Audio output timeline data |
| `cpu_timeline` | Int | CPU usage timeline |
| `disk_timeline` | Int | Disk usage timeline |
| `network_timeline` | Int | Network usage timeline |
| `mbb_timeline` | Int | Mobile broadband usage timeline |
