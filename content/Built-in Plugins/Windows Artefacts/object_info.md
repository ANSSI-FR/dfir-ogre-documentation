---
 title: 'Object Info'
---


{{< callout type="important" >}}Data Type: **objinfo** \
	Python Parser: **Csv**{{< /callout >}}

### Description 

Each row represents a Windows object-manager namespace entry captured by GetObjInfo, with object type, name, namespace path, symbolic-link target, and link creation time where available. Use it to find suspicious mutexes, devices, or redirections and correlate named objects with processes. The namespace is transient, so the output reflects collection-time state rather than historical activity.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `object_name`   |
|Additional Description    | `object_path`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `computer_name` | String | Host name that produced the GetObjInfo report |
| `operating_system` | String | Operating system version string (e.g., 'Windows Server 2016 Standard Edition') |
| `object_type` | String | Type of Windows object (Mutant, Type, Directory, SymbolicLink, etc.) |
| `object_name` | String | Name of the Windows object in the namespace |
| `object_path` | String | Full path of the object in the object manager namespace |
| `link_target` | String | Target path that a symbolic link points to (empty if not applicable) |
| `link_creation_time` | DateTime | Timestamp when the link was created |
| `description` | String | Additional description or metadata about the object |
