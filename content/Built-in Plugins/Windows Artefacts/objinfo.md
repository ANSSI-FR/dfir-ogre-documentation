---
 title: 'Objinfo'
---


{{< callout type="important" >}}Data Type: **objinfo** \
	Python Parser: **Csv**{{< /callout >}}

### Description 

Parses files produced by the GetObjInfo utility, extracting Windows object information from the object manager namespace.

- Object type indicates whether the entry is a directory, mutex, symbolic link, etc.
- Object name and path uniquely identify each object in the namespace.
- Link target shows where a symbolic link points to when present.
- Creation time records when a link was established.


### Timeline 

{{< callout type="warning" >}}This plugin does not contains timestamped data and cannot be used to create a timeline{{< /callout >}}
### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `computer_name` | String |  | Host name that produced the GetObjInfo report |
| `operating_system` | String |  | Operating system version string (e.g., 'Windows Server 2016 Standard Edition') |
| `object_type` | String |  | Type of Windows object (Mutant, Type, Directory, SymbolicLink, etc.) |
| `object_name` | String |  | Name of the Windows object in the namespace |
| `object_path` | String |  | Full path of the object in the object manager namespace |
| `link_target` | String |  | Target path that a symbolic link points to (empty if not applicable) |
| `link_creation_time` | DateTime |  | Timestamp when the link was created |
| `description` | String |  | Additional description or metadata about the object |
