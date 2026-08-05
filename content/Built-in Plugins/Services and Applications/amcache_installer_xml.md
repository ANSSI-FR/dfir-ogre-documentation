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

| Output Name | Data Type | Description |
|---|---|---|
| `name` | String | Name of the installed executable |
| `complete` | String | Completion state of the installer session |
| `program_id` | String | Program ID associated with the install |
| `created_arp_entries` | String | Number of Add/Remove Programs entries created |
| `start_time` | DateTime | Installer session start time |
| `stop_time` | DateTime | Installer session end time |
| `short_name` | String | Short (8.3) name of the installed executable |
| `is_os_component` | String | Whether the installer is an OS component |
| `size` | IntRadix | Size of the installed executable in bytes |
| `pe_header_hash` | String | Hash of the PE header |
| `image_size` | IntRadix | Size of the executable image in memory |
| `pe_checksum` | String | PE image checksum |
| `link_date` | String | PE link (compilation) date |
| `linker_version` | String | PE linker version |
| `bin_file_version` | String | Binary file version |
| `bin_product_version` | String | Binary product version |
| `binary_type` | String | PE binary type (exe, dll, driver) |
| `created` | DateTime | Installed executable creation timestamp |
| `modified` | DateTime | Installed executable modification timestamp |
| `version_language` | String | Language code of the installed executable |
| `sha1` | String | SHA-1 hash of the installed executable |
| `sig_publisher_name` | String | Publisher name from the signature |
| `file_version` | String | Installed executable file version |
| `company` | String | Company (vendor) name |
| `file_description` | String | File description string |
| `product` | String | Product name |
| `long_path_hash` | String | Hash of the long path storing the executable |
