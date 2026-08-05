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
| `indicators[].name` | String | File name |
| `indicators[].file` | String | File path from the static property |
| `indicators[].run` | String | Registry key/value that launched the program |
| `files[]` | Array[Object] |  |
| `files[].name` | String | File name |
| `files[].sha1` | String | SHA-1 hash of the file |
| `files[].size` | IntRadix | File size in bytes |
| `files[].product` | String | Product name |
| `files[].company` | String | Company (vendor) name |
| `files[].product_version` | String | Product version |
| `files[].version_language` | String | Language code of the file |
| `files[].file_version` | String | File version number |
| `files[].image_size` | IntRadix | Size of the executable image in bytes |
| `files[].file_description` | String | File description string |
| `files[].linker_version` | String | PE linker version |
| `files[].link_date` | DateTime | PE link (compilation) date |
| `files[].binary_type` | String | PE binary type (exe, dll, driver) |
| `files[].created` | DateTime | File creation timestamp |
| `files[].modified` | DateTime | File modification timestamp |
| `files[].long_path_hash` | String | Hash of the long path storing the file |
| `files[].unique_id` | String | Unique identifier of the file entry |
