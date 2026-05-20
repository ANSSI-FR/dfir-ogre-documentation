---
 title: 'Srum Energy Usage'
---


{{< callout type="important" >}}Data Type: **srum_energy_usage** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Srum table that tracks stores the per‑process estimates of how much electrical
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
| `EventTimestamp` | Int |  |  |
| `StateTransition` | Int |  |  |
| `DesignedCapacity` | Int |  |  |
| `FullChargedCapacity` | Int |  |  |
| `ChargeLevel` | Int |  |  |
| `CycleCount` | Int |  |  |
| `ConfigurationHash` | Int |  |  |
