---
 title: 'Fastfind Registry'
---


{{< callout type="important" >}}Data Type: **fastfind_reg** \
	Python Parser: **XML**{{< /callout >}}

### Description 

Each row is a Registry match returned by FastFind, with hive, key and value paths, value data, key timestamp, and volume or snapshot context. Use it to locate configuration, persistence, or indicator hits across hives and snapshots. Results reflect the configured search, and a key LastWrite time is not a per-value modification time.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `description`   |
|    | `hive_path`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `volume_id` | String |  |  |
| `snapshot_id` | String |  |  |
| `hive_path` | String | FILE_PATH |  |
| `description` | String |  |  |
| `key[]` | Array[Object] |  |  |
| `key[].key` | String | KEY_PATH |  |
| `key[].subkeys_count` | Int |  |  |
| `key[].values_count` | Int |  |  |
| `key[].lastmodified_key` | DateTime | DATE_MODIFICATION |  |
| `value[]` | Array[Object] |  |  |
| `value[].key` | String | KEY_PATH |  |
| `value[].value` | String | VALUE_NAME |  |
| `value[].type` | String |  |  |
| `value[].data_size` | Int |  |  |
| `value[].lastmodified_key` | DateTime | DATE_MODIFICATION |  |
