---
 title: 'Volstats'
---


{{< callout type="important" >}}Data Type: **volstats** \
	Python Parser: **Csv**{{< /callout >}}

### Description 

Each row describes a volume observed by ORC, with host, volume identifier, mount point or device location, volume type, shadow-copy identifier, and indicators of which artifact sets were collected. Use it to map paths and records to the correct live volume or snapshot. It is collection metadata and does not itself represent file or user activity.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `mount_point`   |
|    | `volumeid`   |
|Additional Description    | `volume_type`   |
|    | `location`   |
|    | `shadow_copy`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `computer_name` | String | Host name that produced the volstat report |
| `volumeid` | String | Unique identifier (GUID) of the volume |
| `location` | String | Physical location or drive letter of the volume |
| `volume_type` | String | File system type (FAT, NTFS, etc.) |
| `is_parsed` | Bool | Whether the volume was successfully parsed |
| `mount_point` | String | Path where the volume is mounted |
| `shadow_copy` | Python | Identifier of the associated VSS snapshot, if any |
| `fileinfo` | String | raw file‑information from the volume |
| `i30info` | String | directory index ($I30) information for the volume |
| `attrinfo` | String | NTFS attribute information for the volume |
| `timeline` | String | timeline metadata (e.g., timestamps) associated with the volume |
| `secdescr` | String | security descriptor data for the volume |
