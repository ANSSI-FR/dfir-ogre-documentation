---
 title: 'Amcache Installer Xml'
---


{{< callout type="important" >}}Data Type: **amcache_installer_xml** \
	Python Parser: **XML**{{< /callout >}}

### Description 

Each row describes installed-software evidence from an Amcache XML report, including program identity, observed times, hash, publisher, and executable metadata. Use it to correlate software inventory with files and host activity. The report is a point-in-time inventory and does not by itself prove installation time or execution.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `name`   |
|Additional Description    | `product`   |
|    | `company`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `name` | String |  |  |
| `complete` | String |  |  |
| `program_id` | String |  |  |
| `created_arp_entries` | String |  |  |
| `start_time` | DateTime |  |  |
| `stop_time` | DateTime |  |  |
| `short_name` | String |  |  |
| `is_os_component` | String |  |  |
| `size` | IntRadix |  |  |
| `pe_header_hash` | String |  |  |
| `image_size` | IntRadix |  |  |
| `pe_checksum` | String |  |  |
| `link_date` | String |  |  |
| `linker_version` | String |  |  |
| `bin_file_version` | String |  |  |
| `bin_product_version` | String |  |  |
| `binary_type` | String |  |  |
| `created` | DateTime |  |  |
| `modified` | DateTime |  |  |
| `version_language` | String |  |  |
| `sha1` | String |  |  |
| `sig_publisher_name` | String |  |  |
| `file_version` | String |  |  |
| `company` | String |  |  |
| `file_description` | String |  |  |
| `product` | String |  |  |
| `long_path_hash` | String |  |  |
