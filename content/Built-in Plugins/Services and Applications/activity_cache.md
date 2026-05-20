---
 title: 'Activity Cache'
---


{{< callout type="important" >}}Data Type: **activity_cache** \
	Python Parser: **SQLite**{{< /callout >}}

### Description 

Extracts rows from the *Activity* SQLite table that records Windows 10 Timeline events. Each row represents a user‑initiated action, linking an application to a time span and optional payload data.

- Provides a chronological view of user activity across applications.
- Captures start / end timestamps for precise temporal analysis.
- Stores raw payload for deeper forensic investigation of the activity context.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `app_id`   |
|    | `group`   |
|Additional Description    | `app_activity_id`   |
|    | `payload`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `app_id` | String |  | identifier of the application that generated the activity |
| `app_activity_id` | String |  | unique identifier for the specific activity event |
| `group` | String |  | grouping value used to categorize related activities |
| `tag` | String |  | optional tag associated with the activity |
| `payload` | String |  | raw payload data (e.g., JSON) containing additional activity details |
| `created_in_cloud` | DateTime |  | timestamp when the activity was created or synced in the cloud |
| `start_time` | DateTime |  | timestamp marking the start of the activity |
| `end_time` | DateTime |  | timestamp marking the end of the activity |
| `last_modified_on_client` | DateTime |  | local client timestamp of the last modification to the activity record |
| `original_last_modified_on_client` | DateTime |  | original client timestamp before any subsequent modifications |
