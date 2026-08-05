---
 title: 'Amcache Program Previous'
---


{{< callout type="important" >}}Data Type: **amcache_program_xml** \
	Python Parser: **XML**{{< /callout >}}

### Description 

Each row is a program inventory entry from an AEINV PREVIOUS report, with program identity, version, publisher, source, paths, and related executable hashes where available. Use it to recover earlier inventory and correlate software across reports. Presence in the report does not by itself prove execution.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `name`   |
|Additional Description    | `version`   |
|    | `publisher`   |
|    | `source`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `id` | String | APP_ID | Program identifier |
| `name` | String | APP_NAME | Program name |
| `version` | String | PE_VERSION | Program version |
| `publisher` | String | PUBLISHER | Program publisher |
| `source` | String |  | Installation method ('MSI', 'AppxPackage', 'AddRemoveProgram') |
| `indicators[]` | Array[Object] |  |  |
| `indicators[].name` | String |  |  |
| `indicators[].file` | String |  |  |
| `indicators[].run` | String |  |  |
| `files[]` | Array[Object] |  |  |
| `files[].name` | String |  |  |
| `files[].sha1` | String |  |  |
| `files[].size` | IntRadix |  |  |
| `files[].product` | String |  |  |
| `files[].company` | String |  |  |
| `files[].product_version` | String |  |  |
| `files[].version_language` | String |  |  |
| `files[].file_version` | String |  |  |
| `files[].image_size` | IntRadix |  |  |
| `files[].file_description` | String |  |  |
| `files[].linker_version` | String |  |  |
| `files[].link_date` | DateTime |  |  |
| `files[].binary_type` | String |  |  |
| `files[].created` | DateTime |  |  |
| `files[].modified` | DateTime |  |  |
| `files[].long_path_hash` | String |  |  |
| `files[].unique_id` | String |  |  |
