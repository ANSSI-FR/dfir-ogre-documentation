---
 title: 'Vss Snapshot'
---


{{< callout type="important" >}}Data Type: **vss_snapshot** \
	Python Parser: **Csv**{{< /callout >}}

### Description 

Each row describes a Volume Shadow Copy snapshot, with snapshot identifier, source volume, device path, creation time, and snapshot attributes. Use it to anchor historical artifact versions and correlate records to a specific snapshot. Snapshot metadata does not guarantee that every file or artifact was retained, readable, or collected.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `volume_name`   |
|Additional Description    | `device_instance`   |
|    | `snapshot_id`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `snapshot_id` | Python |  | GUID identifying the VSS snapshot |
| `device_instance` | String |  | Device path of the shadow copy (e.g. \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1) |
| `volume_name` | String |  | Original volume that the snapshot belongs to |
| `creation_time` | DateTime |  | Timestamp when the snapshot was created |
| `attributes` | Split |  | Combined VSS attribute flags (e.g. VSS_VOLSNAP_ATTR_PERSISTENT|…) |
