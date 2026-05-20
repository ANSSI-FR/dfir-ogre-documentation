---
 title: 'Browser Download History Lite'
---


{{< callout type="important" >}}Data Type: **browser_download_history** \
	Python Parser: **SQLite**{{< /callout >}}

### Description 

Extracts records from the `places` sqlite database that Firefox uses to store download
metadata. Each row contains the path of the saved file, the source URL, file size and
timestamps for the start and end of the download.

- Reveals which URLs were downloaded and where they were saved.
- Provides the total byte count of each download.
- Indicates whether a download entry has been removed (deleted flag).


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
