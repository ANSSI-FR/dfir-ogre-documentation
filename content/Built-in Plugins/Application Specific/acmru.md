---
 title: 'Acmru'
---


{{< callout type="important" >}}Data Type: **acmru** \
	Python Parser: **RegAcMru**{{< /callout >}}

### Description 

Each row is a Windows XP Search Assistant query recovered from a per-user hive, with search category, query text, MRU order, registry provenance, and key LastWrite time. Use it to reconstruct user search intent and pivot on filenames, hosts, or terms. Only the newest indexed entry is associated with the category key time; other queries have no individual timestamp.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `search_request`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `search_request` | String | search query entered in the Windows Search Assistant |
| `order_index` | Int | Zero-based position of the query in the category MRU |
| `category` | String | Windows XP Search Assistant category identifier |
| `key_path` | String | full registry key name |
| `key_modif_time` | DateTime | last modification timestamp of the registry key |
| `key_security` | Object |  |
| `key_security.owner_sid` | String | SID of the user that owns the registry key |
| `key_security.group_sid` | String | SID of the group that owns the registry key |
| `key_security.control_flags[]` | Array[String] | security descriptor control flags for the key |
| `key_security.sacl_aces[]` | Array[Object] |  |
| `key_security.sacl_aces[].ace_type` | String | type of ACE (e.g., allow, deny) |
| `key_security.sacl_aces[].ace_flags[]` | Array[String] | ACE flags that modify inheritance or behavior |
| `key_security.sacl_aces[].rights[]` | Array[String] | permissions granted or denied by the ACE |
| `key_security.sacl_aces[].account_sid` | String | SID of the account the ACE applies to |
| `key_security.sacl_aces[].ace_size` | Int | declared ACE size in bytes |
| `key_security.sacl_aces[].object_type_guid` | String | GUID identifying the object type governed by the ACE |
| `key_security.sacl_aces[].inherited_object_type_guid` | String | GUID identifying the inherited object type governed by the ACE |
| `key_security.sacl_aces[].raw_hex` | String | raw ACE bytes preserved as hexadecimal |
| `key_security.dacl_aces[]` | Array[Object] |  |
| `key_security.dacl_aces[].ace_type` | String | type of ACE (e.g., allow, deny) |
| `key_security.dacl_aces[].ace_flags[]` | Array[String] | ACE flags that modify inheritance or behavior |
| `key_security.dacl_aces[].rights[]` | Array[String] | permissions granted or denied by the ACE |
| `key_security.dacl_aces[].account_sid` | String | SID of the account the ACE applies to |
| `key_security.dacl_aces[].ace_size` | Int | declared ACE size in bytes |
| `key_security.dacl_aces[].object_type_guid` | String | GUID identifying the object type governed by the ACE |
| `key_security.dacl_aces[].inherited_object_type_guid` | String | GUID identifying the inherited object type governed by the ACE |
| `key_security.dacl_aces[].raw_hex` | String | raw ACE bytes preserved as hexadecimal |
