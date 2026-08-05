---
 title: 'Fastfind Object'
---


{{< callout type="important" >}}Data Type: **fastfind_obj** \
	Python Parser: **XML**{{< /callout >}}

### Description 

Each row is a Windows object-manager match returned by FastFind, with object type, name, namespace path, and match description. Use it to identify suspicious named objects or namespace links and correlate them with processes or malware indicators. The result is bounded by the search criteria and collection-time namespace state.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `description`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `description` | String | Match description returned by FastFind |
| `object[]` | Array[Object] |  |
| `object[].type` | String | Object type (e.g., file, folder) |
| `object[].name` | String | Object name |
| `object[].path` | String | Path to the object |
