---
 title: 'Evt'
---


{{< callout type="important" >}}Data Type: **evt** \
	Python Parser: **WinEvt**{{< /callout >}}

### Description 

Parse Windows EventLog (EVT) files and emit one record per event.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `provider_name`   |
|    | `event_id`   |
|Additional Description    | `event_data`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `provider_name` | String |  | Name of the source that generated the event. |
| `event_id` | Int |  | Identifier of the event (lower 16 bits of the record identifier). |
| `event_type` | Int |  | Event type (e.g. error, warning, information). |
| `record_number` | Int |  | Sequential number of the event record in the EVT file. |
| `offset` | Int |  | Byte offset of the record from the start of the EVT file. |
| `recovered` | Bool |  | True if the record was recovered (partially overwritten). |
| `facility` | Int |  | Facility code extracted from the event identifier. |
| `severity` | Int |  | Severity level extracted from the event identifier. |
| `message_identifier` | Int |  | Full 32‑bit message identifier. |
| `event_category` | Int |  | Category of the event. |
| `computer_name` | String |  | Computer name stored in the event record. |
| `user_sid` | String | USER_ID | User security identifier (SID) associated with the event. |
| `event_data[]` | Array[String] |  | Array of strings attached to the event. |
| `creation_time` | DateTime | DATE_CREATION | Timestamp when the event record was created. |
| `written_time` | DateTime |  | Timestamp when the event record was written to the log. |
