---
 title: 'Volstats'
---


{{< callout type="important" >}}Data Type: **volstats** \
	Python Parser: **Csv**{{< /callout >}}

### Description 

Parses a Windows volume‑statistics csv file. Each line describes:.

- Computer name identifies the host that exported the volume list.
- Volume ID and mount point uniquely reference the volume on the system.
- Volume type indicates whether the volume is fixed, removable, etc.
- Shadow‑copy ID links the entry to a specific VSS snapshot when present.
- etc.


### Timeline 

{{< callout type="warning" >}}This plugin does not contains timestamped data and cannot be used to create a timeline{{< /callout >}}
### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `computer_name` | String |  | Host name that produced the volstat report |
| `volumeid` | String |  | Unique identifier (GUID) of the volume |
| `location` | String |  | Physical location or drive letter of the volume |
| `volume_type` | String |  | File system type (FAT, NTFS, etc.) |
| `is_parsed` | Bool |  |  |
| `mount_point` | String |  | Path where the volume is mounted |
| `shadow_copy` | String |  | Identifier of the associated VSS snapshot, if any |
| `fileinfo` | String |  | raw file‑information from the volume |
| `i30info` | String |  | directory index ($I30) information for the volume |
| `attrinfo` | String |  | NTFS attribute information for the volume |
| `timeline` | String |  | timeline metadata (e.g., timestamps) associated with the volume |
| `secdescr` | String |  | security descriptor data for the volume |
