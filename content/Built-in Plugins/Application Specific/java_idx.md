---
 title: 'Java Idx'
---


{{< callout type="important" >}}Data Type: **java_idx** \
	Python Parser: **JavaIdx**{{< /callout >}}

### Description 

Each row describes an artifact recorded in a Java deployment cache index, with source URL, server IP, size, cache state, signing flag, request data, and modification or expiry times. Use it to trace Java-delivered content and correlate cached files with network or execution evidence. Cache presence and a signing flag do not prove successful execution or trustworthiness.


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
