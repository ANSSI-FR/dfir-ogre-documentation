---
 title: 'Amcache Program Wer'
---


{{< callout type="important" >}}Data Type: **amcache_program_xml** \
	Python Parser: **XML**{{< /callout >}}

### Description 

Each row is a program inventory entry from an AEINV Windows Error Reporting XML report, with program identity, version, publisher, source, paths, and related executable hashes where available. Use it to correlate software and binaries seen by the reporting process. Presence does not by itself prove execution.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `name`   |
|Additional Description    | `version`   |
|    | `publisher`   |
|    | `source`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `id` | String | Program identifier |
| `name` | String | Program name |
| `version` | String | Program version |
| `publisher` | String | Program publisher |
| `source` | String | Installation method ('MSI', 'AppxPackage', 'AddRemoveProgram') |
| `indicators[]` | Array[Object] |  |
| `indicators[].name` | String |  |
| `indicators[].file` | String |  |
| `indicators[].run` | String |  |
| `files[]` | Array[Object] |  |
| `files[].name` | String |  |
| `files[].sha1` | String |  |
| `files[].size` | IntRadix |  |
| `files[].product` | String |  |
| `files[].company` | String |  |
| `files[].product_version` | String |  |
| `files[].version_language` | String |  |
| `files[].file_version` | String |  |
| `files[].image_size` | IntRadix |  |
| `files[].file_description` | String |  |
| `files[].linker_version` | String |  |
| `files[].link_date` | DateTime |  |
| `files[].binary_type` | String |  |
| `files[].created` | DateTime |  |
| `files[].modified` | DateTime |  |
| `files[].long_path_hash` | String |  |
| `files[].unique_id` | String |  |
