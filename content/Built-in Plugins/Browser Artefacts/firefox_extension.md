---
 title: 'Firefox Extension'
---


{{< callout type="important" >}}Data Type: **firefox_extension** \
	Python Parser: **FirefoxExtension**{{< /callout >}}

### Description 

Extracts metadata from Firefox browser add‑ons (version 26+). It parses each extension’s
manifest to retrieve identifiers, version information, installation path and declared
permissions.

- Reveals which extensions are present on a system.
- Provides version and source details for each add‑on.
- Lists required, optional and user‑granted permissions.
- Includes installation and update timestamps.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `name`   |
|    | `browser`   |
|Additional Description    | `description`   |
|    | `path`   |
|    | `update_url`   |
|    | `source_uri`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `name` | String |  | display name of the Firefox add‑on |
| `browser` | String |  | browser name (always 'firefox') |
| `type` | String |  | type/category of the add‑on (e.g., extension, theme) |
| `description` | String |  | human‑readable description of the add‑on |
| `id` | String |  | unique identifier of the add‑on |
| `version` | String |  | version string of the add‑on |
| `path` | String |  | filesystem path where the add‑on is installed |
| `update_url` | String |  | URL used by the add‑on to check for updates |
| `source_uri` | String |  | original source URI from which the add‑on was obtained |
| `root_uri` | String |  | root URI of the add‑on package |
| `user_permissions` | Object |  |  |
| `user_permissions.permissions[]` | Array[String] |  |  |
| `user_permissions.origins[]` | Array[String] |  |  |
| `user_permissions.data_collection[]` | Array[String] |  |  |
| `optional_permissions` | Object |  |  |
| `optional_permissions.permissions[]` | Array[String] |  |  |
| `optional_permissions.origins[]` | Array[String] |  |  |
| `optional_permissions.data_collection[]` | Array[String] |  |  |
| `requested_permissions` | Object |  |  |
| `requested_permissions.permissions[]` | Array[String] |  |  |
| `requested_permissions.origins[]` | Array[String] |  |  |
| `requested_permissions.data_collection[]` | Array[String] |  |  |
| `install_date` | DateTime | DATE_INSTALLATION |  |
| `update_date` | DateTime | DATE_MODIFICATION |  |
