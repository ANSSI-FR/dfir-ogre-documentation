---
 title: 'Backup Exclude'
---


{{< callout type="important" >}}Data Type: **backup_exclude** \
	Python Parser: **RegSnapExclude**{{< /callout >}}

### Description 

Extracts entries that Windows marks as excluded from Volume Shadow Copy Service (VSS) and backup operations, from the `System` hive.

- Provides a list of files/folders purposely omitted from snapshots.
- Includes the registry key location, modification time and security owner.
- Outputs data in a timeline‑compatible JSON‑L format for further analysis.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `name`   |
|Additional Description    | `file_path`   |
|    | `type`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `type` | String |  | type of the excluded entry (e.g., file or folder) |
| `name` | String |  | display name of the excluded item |
| `file_path` | String |  | full filesystem path of the excluded file or folder |
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
