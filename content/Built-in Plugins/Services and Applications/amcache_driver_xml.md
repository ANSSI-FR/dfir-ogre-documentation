---
 title: 'Amcache Driver Xml'
---


{{< callout type="important" >}}Data Type: **amcache_driver_xml** \
	Python Parser: **XML**{{< /callout >}}

### Description 

Each row is a driver inventory entry extracted from an Amcache XML report, with hash, name, version, vendor, size, and compilation metadata. Use these attributes to identify unusual or vulnerable drivers and correlate binaries across hosts. Inventory presence does not establish that the driver loaded or executed.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `name`   |
|Additional Description    | `product`   |
|    | `company`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `sha1` | String | SHA-1 hash of the driver binary |
| `name` | String | Driver name |
| `type` | String | Driver type (e.g. Kernel, File System) |
| `version` | String | Driver version |
| `compilation_date` | DateTime | Driver compilation/link timestamp |
| `checksum` | String | Driver image checksum |
| `image_size` | IntRadix | Driver binary size in bytes |
| `company` | String | Driver vendor/company name |
| `product` | String | Driver product name |
| `product_version` | String | Driver product version |
| `wdf_version` | String | Windows Driver Framework version |
