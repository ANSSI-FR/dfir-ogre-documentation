---
 title: 'Srum Energy Usage'
---


{{< callout type="important" >}}Data Type: **srum_energy_usage** \
	Python Parser: **Srum**{{< /callout >}}

### Description 

Each row is an SRUM battery or power-state event, with timestamp, state transition, designed or full capacity, charge level, cycle count, and configuration hash. Use it to reconstruct device power conditions around user or system activity. These are system energy-state records, not per-process consumption measurements.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `user_id`   |
|Description    | `app_id`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `incremental_id` | Int | Auto-increment identifier of the SRUM record |
| `timestamp` | DateTime | Timestamp of the SRUM record |
| `app_id` | String | Identifier of the application |
| `user_id` | String | Identifier (SID) of the user |
| `EventTimestamp` | Int |  |
| `StateTransition` | Int |  |
| `DesignedCapacity` | Int |  |
| `FullChargedCapacity` | Int |  |
| `ChargeLevel` | Int |  |
| `CycleCount` | Int |  |
| `ConfigurationHash` | Int |  |
