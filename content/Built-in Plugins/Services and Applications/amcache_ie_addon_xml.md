---
 title: 'Amcache Ie Addon Xml'
---


{{< callout type="important" >}}Data Type: **amcache_ie_addon_xml** \
	Python Parser: **XML**{{< /callout >}}

### Description 

Each row identifies an Internet Explorer add-on found in an Amcache XML report, including its identifier, name, type, and publisher. Use it to inventory browser integrations and pivot on suspicious publishers or identifiers. Report presence does not show that the add-on was enabled or used.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `name`   |
|Additional Description    | `type`   |
|    | `publisher`   |
|    | `id`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `id` | Python | APP_ID | Program identifier |
| `name` | String | APP_NAME | Program name |
| `type` | String |  | AddOn type |
| `publisher` | String | PUBLISHER | Program publisher |
