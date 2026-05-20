---
 title: 'Browser Download History'
---


{{< callout type="important" >}}Data Type: **browser_download_history** \
	Python Parser: **SQLite**{{< /callout >}}

### Description 

Parses the download history database of a Chrome profile (typically `*/Default/History`). It enables analysts to reconstruct what files a user obtained from the web, when the download started and finished, how much data was transferred, and whether the file was opened or flagged as dangerous.

- URL of the downloaded resource.
- Local path where Chrome saved the file.
- Byte counts: received vs. total size.
- Start/end timestamps, download state, danger type, interruption reason and whether the file was opened.


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
