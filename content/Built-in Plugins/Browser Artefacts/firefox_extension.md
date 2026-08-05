---
 title: 'Firefox Extension'
---


{{< callout type="important" >}}Data Type: **firefox_extension** \
	Python Parser: **FirefoxExtension**{{< /callout >}}

### Description 

Each row describes a Firefox add-on, including identity, version, install path, source, declared permissions or origins, and install or update times. Use it to assess extension provenance and capability or hunt for risky permissions and unexpected installation sources. Declared capability is not observed behavior, and the snapshot can miss removed add-ons.


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

| Output Name | Data Type | Description |
|---|---|---|
| `name` | String | display name of the Firefox add‑on |
| `browser` | String | browser name (always 'firefox') |
| `type` | String | type/category of the add‑on (e.g., extension, theme) |
| `description` | String | human‑readable description of the add‑on |
| `id` | String | unique identifier of the add‑on |
| `version` | String | version string of the add‑on |
| `path` | String | filesystem path where the add‑on is installed |
| `update_url` | String | URL used by the add‑on to check for updates |
| `source_uri` | String | original source URI from which the add‑on was obtained |
| `root_uri` | String | root URI of the add‑on package |
| `user_permissions` | Object |  |
| `user_permissions.permissions[]` | Array[String] | Permission (API) requested or granted to the add-on |
| `user_permissions.origins[]` | Array[String] | Origin or match pattern the permission applies to |
| `user_permissions.data_collection[]` | Array[String] | Kind of data the permission allows collecting |
| `optional_permissions` | Object |  |
| `optional_permissions.permissions[]` | Array[String] | Permission (API) requested or granted to the add-on |
| `optional_permissions.origins[]` | Array[String] | Origin or match pattern the permission applies to |
| `optional_permissions.data_collection[]` | Array[String] | Kind of data the permission allows collecting |
| `requested_permissions` | Object |  |
| `requested_permissions.permissions[]` | Array[String] | Permission (API) requested or granted to the add-on |
| `requested_permissions.origins[]` | Array[String] | Origin or match pattern the permission applies to |
| `requested_permissions.data_collection[]` | Array[String] | Kind of data the permission allows collecting |
| `install_date` | DateTime | Date the add-on was installed |
| `update_date` | DateTime | Date the add-on was last updated |
