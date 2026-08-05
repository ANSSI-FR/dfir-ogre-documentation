---
 title: 'Chrome Download History'
---


{{< callout type="important" >}}Data Type: **browser_download_history** \
	Python Parser: **SQLite**{{< /callout >}}

### Description 

Each row represents a Chrome download record, linking the source URL to the saved path, start and end times, byte counts, state, interruption or danger status, and opened flag. Use it to trace file acquisition and correlate downloads with filesystem or execution evidence. A record can describe an interrupted, removed, or otherwise incomplete download.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `url`   |
|Additional Description    | `received_bytes`   |
|    | `total_bytes`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `target_path` | String |  | local filesystem path where Chrome saved the downloaded file |
| `url` | String |  | original URL of the downloaded resource |
| `received_bytes` | Int |  | number of bytes actually received for the download |
| `total_bytes` | Int |  | expected total size of the downloaded file in bytes |
| `start_time` | DateTime |  | timestamp when the download started |
| `end_time` | DateTime |  | timestamp when the download finished or was interrupted |
| `state` | Int |  | numeric code representing the download's state (e.g., in‑progress, completed) |
| `danger_type` | Int |  | numeric identifier indicating if the download was flagged as dangerous |
| `interrupt_reason` | Int |  | code describing why the download was interrupted |
| `opened` | Int |  | flag (0/1) indicating whether the downloaded file was opened by the user |
