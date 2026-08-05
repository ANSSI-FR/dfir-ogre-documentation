---
 title: 'Ie Webcache History'
---


{{< callout type="important" >}}Data Type: **ie_webcache_history** \
	Python Parser: **IeWebCache**{{< /callout >}}

### Description 

Each row is an Internet Explorer or legacy WebCache container record, with URL, cached filename, request or response properties, access counts, and creation, access, modification, synchronization, or expiry times. Use it to reconstruct browsing and cached-resource activity. Cache records may arise from redirects or background content, and timestamp meaning varies by container.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `url`   |
|Additional Description    | `filename`   |
|    | `access_count`   |
|    | `file_size`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `file_size` | Int | Size of the cached file in bytes |
| `type` | Int | Record type identifier from WebCache |
| `flags` | Int | Flags associated with the cache entry |
| `access_count` | Int | Number of times this URL was accessed |
| `sync_count` | Int | Number of synchronization operations for this entry |
| `exemption_delta` | Int | Time offset exemption delta in seconds |
| `url` | String | Visited URL |
| `filename` | String | Cached file name (if applicable) |
| `file_extension` | String | File extension of the cached resource |
| `redirect_url` | String | Redirect target URL (if any) |
| `request_headers` | String | HTTP request headers (hex encoded) |
| `response_properties[]` | Array[Object] |  |
| `response_properties[].store_index` | Int | Zero-based serialized property store index |
| `response_properties[].storage_index` | Int | Zero-based property storage index within the store |
| `response_properties[].format_id` | String | Property set format identifier (FMTID) |
| `response_properties[].id` | Int | Property identifier within the property set |
| `response_properties[].name` | String | Known symbolic property name, when available |
| `response_properties[].value_type` | String | Windows variant property type |
| `response_properties[].value` | String | Decoded property value represented as a string |
| `response_properties_raw` | String | Original serialized response properties (hex encoded) |
| `response_properties_parse_error` | String | Non-fatal errors encountered while decoding response properties |
| `group` | String | Cache group identifier (hex encoded) |
| `sync_date` | DateTime | Last synchronization time in UTC |
| `creation_date` | DateTime | Entry creation timestamp in UTC |
| `expiry_date` | DateTime | Expiration timestamp in UTC |
| `modified_date` | DateTime | Last modification timestamp in UTC |
| `accessed_date` | DateTime | Last access timestamp in UTC |
| `post_check_date` | DateTime | Time of last post-check validation in UTC |
