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

| Output Name | Data Type | Description |
|---|---|---|
| `volume_id` | String | Volume identifier of the hive source |
| `snapshot_id` | String | Snapshot identifier the hive was read from |
| `hive_path` | String | Path to the registry hive |
| `description` | String | Match description returned by FastFind |
| `key[]` | Array[Object] |  |
| `key[].key` | String | Full registry key path |
| `key[].subkeys_count` | Int | Number of subkeys in the key |
| `key[].values_count` | Int | Number of values in the key |
| `key[].lastmodified_key` | DateTime | Key last-write timestamp (UTC) |
| `value[]` | Array[Object] |  |
| `value[].key` | String | Full registry key path |
| `value[].value` | String | Name of the registry value |
| `value[].type` | String | Registry value data type (e.g., REG_SZ) |
| `value[].data_size` | Int | Size of the value data in bytes |
| `value[].lastmodified_key` | DateTime | Key last-write timestamp (UTC) |
