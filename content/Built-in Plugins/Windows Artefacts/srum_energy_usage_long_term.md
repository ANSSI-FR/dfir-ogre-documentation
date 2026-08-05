---
 title: 'Srum Energy Usage Long Term'
---


{{< callout type="important" >}}Data Type: **srum_energy_usage_long_term** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Each row is an SRUM long-term power summary, with active or connected-standby time on AC or DC power, discharge duration and energy, battery capacity, cycle count, and configuration hash. Use it to establish broader power and uptime context. Values are aggregated system totals rather than discrete events or per-process measurements.


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
| `active_ac_time` | Int |  |  |
| `cs_ac_time` | Int |  |  |
| `active_dc_time` | Int |  |  |
| `cs_dc_time` | Int |  |  |
| `active_discharge_time` | Int |  |  |
| `cs_discharge_time` | Int |  |  |
| `active_energy` | Int |  |  |
| `cs_energy` | Int |  |  |
| `designed_capacity` | Int |  |  |
| `full_charged_capacity` | Int |  |  |
| `cycle_count` | Int |  |  |
| `configuration_hash` | Int |  |  |
