---
 title: 'Activity Cache'
---


{{< callout type="important" >}}Data Type: **activity_cache** \
	Python Parser: **ActivityCache**{{< /callout >}}

### Description 

Windows Activities Cache records application activities and queued operations across schema versions, with application identifiers, activity type and status, timing, payload, and device context. Use it to reconstruct user activity and correlate application events across devices. The start-time source distinguishes native activity times from last-modified fallbacks.


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
| `record_source` | String |  | source table or merged source tables for this logical version |
| `database_user_version` | Int |  | SQLite PRAGMA user_version recorded for schema provenance |
| `start_time_source` | String |  | native start_time, last_modified_time fallback, or unavailable |
| `id` | String |  | binary-safe activity identifier |
| `app_id` | String |  | application identity definitions associated with the activity |
| `package_id_hash` | String |  | package identity hash |
| `app_activity_id` | String |  | application-defined activity identifier |
| `activity_type` | Int |  | numeric activity type |
| `activity_status` | Int |  | persisted activity status |
| `parent_activity_id` | String |  | identifier of the parent activity |
| `tag` | String |  | application-defined activity tag |
| `group` | String |  | activity grouping value |
| `match_id` | String |  | activity matching identifier |
| `last_modified_time` | DateTime |  | last modification time stored by the service |
| `expiration_time` | DateTime |  | activity expiration time |
| `payload` | String |  | encoded activity payload |
| `priority` | Int |  | activity priority |
| `originating_device` | String |  | legacy originating device value |
| `is_local_only` | Bool |  | whether the activity is restricted to the local device |
| `platform_device_id` | String |  | platform device identifier |
| `dds_device_id` | String |  | Connected Devices Platform device identifier |
| `created_in_cloud` | DateTime |  | cloud creation time |
| `start_time` | DateTime | DATE_START | native or explicitly identified fallback start time |
| `end_time` | DateTime |  | activity end time |
| `last_modified_on_client` | DateTime |  | last client modification time |
| `group_app_activity_id` | String |  | application activity identifier for the group |
| `clipboard_payload` | String |  | encoded clipboard payload |
| `enterprise_id` | String |  | enterprise scope identifier |
| `original_payload` | String |  | encoded original activity payload |
| `user_action_state` | Int |  | numeric user action state |
| `is_read` | Bool |  | whether the activity has been read |
| `original_last_modified_on_client` | DateTime |  | original client modification time |
| `group_items` | String |  | serialized activity group items |
| `local_expiration_time` | DateTime |  | local activity expiration time |
| `e_tag` | Int |  | logical activity version tag |
| `operation_order` | Int |  | ordered ActivityOperation sequence number |
| `operation_type` | Int |  | numeric queued operation type |
| `created_time` | DateTime |  | queued operation creation time |
| `attachments` | String |  | legacy serialized operation attachments |
| `operation_expiration_time` | DateTime |  | queued operation expiration time |
| `correlation_vector` | String |  | operation correlation vector |
| `upload_allowed_by_policy` | Bool |  | whether policy permits uploading the operation |
| `patch_fields` | String |  | encoded operation patch fields |
| `throttle_release_time` | DateTime |  | time at which operation throttling is released |
| `publish_process_status` | Int |  | numeric operation publishing status |
