---
 title: 'Java Idx'
---


{{< callout type="important" >}}Data Type: **java_idx** \
	Python Parser: **JavaIdx**{{< /callout >}}

### Description 

Extracts metadata about each downloaded artifact, including its URL, server IP, size,
timestamps and signing status.

The parser interprets version‑specific structures, handling incomplete or busy downloads, and
converts dates to UTC where possible. All extracted fields are emitted as a structured tuple
for downstream analysis.

- Provides the original download URL and originating IP address.
- Indicates whether the entry is a shortcut or an incomplete download.
- Reports file size, last‑modified, expiration and optional signing flag.
- Normalises timestamps to UTC for reliable chronology.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `url`   |
|    | `ip_address`   |
|Additional Description    | `is_incomplete`   |
|    | `is_shortcut`   |
|    | `content_length`   |
|    | `signed`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `url` | String |  | download URL of the file |
| `ip_address` | String |  | source IP address of the server |
| `is_incomplete` | Bool |  | true if the download was incomplete or still in progress |
| `content_length` | Int | FILE_SIZE | size of the downloaded file in bytes |
| `is_shortcut` | Bool |  | true if the entry represents a shortcut rather than the actual file |
| `version_string` | String |  | version string extracted from the IDX file |
| `namespace` | String |  | namespace associated with the download |
| `signed` | Bool |  | indicates whether the downloaded file is digitally signed |
| `download_date` | DateTime |  | timestamp when the file was downloaded |
| `last_modified_date` | DateTime | DATE_MODIFICATION | last‑modified timestamp reported by the server |
| `expiration_date` | DateTime |  | expiration timestamp of the file or associated resource |
| `validation_date` | DateTime |  | validation timestamp (available in IDX 6.05 format) |
| `request` | Object |  | raw HTTP request metadata extracted from the IDX file |
