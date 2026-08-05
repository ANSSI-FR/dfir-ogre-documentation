---
 title: 'Firefox Download History'
---


{{< callout type="important" >}}Data Type: **browser_download_history** \
	Python Parser: **SQLite**{{< /callout >}}

### Description 

Each row represents Firefox download metadata recovered from the Places database, linking a source URL to a saved path, byte count, start and end times, state, and deletion flag where available. Use it to trace acquisition and correlate files with later activity. A history row does not guarantee the transfer completed or that the file was opened.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `url`   |
|Additional Description    | `total_bytes`   |
|    | `deleted`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `target_path` | String |  | local file system path where the downloaded file was saved |
| `url` | String |  | source URL from which the file was downloaded |
| `total_bytes` | Int |  | total size of the downloaded file in bytes |
| `start_time` | DateTime |  | timestamp when the download started |
| `end_time` | DateTime |  | timestamp when the download finished |
| `state` | Int |  | numeric code representing the download state (e.g., completed, cancelled, in‑progress) |
| `deleted` | Bool |  | boolean flag indicating whether the download entry has been marked as deleted |
