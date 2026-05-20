---
 title: 'Bam Dam'
---


{{< callout type="important" >}}Data Type: **bam_dam** \
	Python Parser: **RegBamDam**{{< /callout >}}

### Description 

Extracts Activity Moderator (BAM/DAM) records from the Windows `System` hive. It parses user‑specific settings to retrieve the executable path and execution time.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `user_sid`   |
|Description    | `exec_path`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `exec_path` | String | FILE_PATH | full path of the executable that was run |
| `user_sid` | String | USER_SID | SID of the user associated with the BAM/DAM entry |
| `exec_time` | DateTime | DATE_LAST_RUN | timestamp when the executable was last executed |
| `key_path` | String | KEY_PATH | full registry key name |
| `key_modif_time` | DateTime | DATE_MODIFICATION | last modification timestamp of the registry key |
| `key_security` | Object |  |  |
| `key_security.owner_sid` | String | USER_SID | SID of the user that owns the registry key |
| `key_security.group_sid` | String |  | SID of the group that owns the registry key |
| `key_security.control_flags[]` | Array[String] |  | security descriptor control flags for the key |
| `key_security.dacl_ace` | Object |  |  |
| `key_security.dacl_ace.ace_type` | String |  | type of ACE (e.g., allow, deny) |
| `key_security.dacl_ace.account_sid` | String |  | SID of the account the ACE applies to |
| `key_security.dacl_ace.ace_flags[]` | Array[String] |  | ACE flags that modify inheritance or behavior |
| `key_security.dacl_ace.rights[]` | Array[String] |  | permissions granted or denied by the ACE |
