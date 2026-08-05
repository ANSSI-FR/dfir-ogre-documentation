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

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `sha1` | String |  |  |
| `name` | String |  |  |
| `type` | String |  |  |
| `version` | String |  |  |
| `compilation_date` | DateTime |  |  |
| `checksum` | String |  |  |
| `image_size` | IntRadix |  |  |
| `company` | String |  |  |
| `product` | String |  |  |
| `product_version` | String |  |  |
| `wdf_version` | String |  |  |
