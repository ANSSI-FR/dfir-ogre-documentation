---
 title: 'Amcache Program Xml'
---


{{< callout type="important" >}}Data Type: **amcache_program_xml** \
	Python Parser: **XML**{{< /callout >}}

### Description 

Parse installed programs from AEINV WER xml reports


### Timeline 

{{< callout type="warning" >}}This plugin does not contains timestamped data and cannot be used to create a timeline{{< /callout >}}
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
