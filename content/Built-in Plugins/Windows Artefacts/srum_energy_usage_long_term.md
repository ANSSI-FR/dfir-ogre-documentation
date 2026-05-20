---
 title: 'Srum Energy Usage Long Term'
---


{{< callout type="important" >}}Data Type: **srum_energy_usage_long_term** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Srum table that tracks long term, per‑process estimates of how much electrical
      energy Windows thinks each component has consumed over time.


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
