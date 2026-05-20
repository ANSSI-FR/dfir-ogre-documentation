---
 title: 'Vss Snapshot'
---


{{< callout type="important" >}}Data Type: **vss_snapshot** \
	Python Parser: **Csv**{{< /callout >}}

### Description 

Parses CSV files that list Volume Shadow Copy (VSS) snapshots.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `volume_name`   |
|Additional Description    | `device_instance`   |
|    | `snapshot_id`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `snapshot_id` | String |  | GUID identifying the VSS snapshot |
| `device_instance` | String |  | Device path of the shadow copy (e.g. \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1) |
| `volume_name` | String |  | Original volume that the snapshot belongs to |
| `creation_time` | DateTime |  | Timestamp when the snapshot was created |
| `attributes` | Split |  | Combined VSS attribute flags (e.g. VSS_VOLSNAP_ATTR_PERSISTENT|…) |
