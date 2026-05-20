---
 title: 'Ie Webcache History'
---


{{< callout type="important" >}}Data Type: **ie_webcache_history** \
	Python Parser: **IeWebCache**{{< /callout >}}

### Description 

Extracts browsing history records from Internet Explorer 10+ WebCache databases (WebCacheV01.dat).
The plugin queries the Containers and Container_X tables to retrieve URL visits with metadata.

- Url provides the visited web address.
- Filename and FileExtension indicate cached file details.
- Timestamps (SyncTime, CreationTime, ExpiryTime, ModifiedTime, AccessedTime) show activity timeline.
- AccessCount and SyncCount reveal frequency and synchronization patterns.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `url`   |
|Additional Description    | `file_name`   |
|    | `access_count`   |
|    | `file_size`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `file_size` | Int |  | Size of the cached file in bytes |
| `type` | Int |  | Record type identifier from WebCache |
| `flags` | Int |  | Flags associated with the cache entry |
| `access_count` | Int |  | Number of times this URL was accessed |
| `sync_count` | Int |  | Number of synchronization operations for this entry |
| `exemption_delta` | Int |  | Time offset exemption delta in seconds |
| `url` | String |  | Visited URL |
| `filename` | String |  | Cached file name (if applicable) |
| `file_extension` | String |  | File extension of the cached resource |
| `redirect_url` | String |  | Redirect target URL (if any) |
| `request_headers` | String |  | HTTP request headers (hex encoded) |
| `response_headers` | String |  | HTTP response headers (hex encoded) |
| `group` | String |  | Cache group identifier (hex encoded) |
| `sync_time` | DateTime |  | Last synchronization time in UTC |
| `creation_time` | DateTime | DATE_CREATION | Entry creation timestamp in UTC |
| `expiry_time` | DateTime |  | Expiration timestamp in UTC |
| `modified_time` | DateTime | DATE_MODIFICATION | Last modification timestamp in UTC |
| `accessed_time` | DateTime | DATE_ACCESS | Last access timestamp in UTC |
| `post_check_time` | DateTime |  | Time of last post-check validation in UTC |
