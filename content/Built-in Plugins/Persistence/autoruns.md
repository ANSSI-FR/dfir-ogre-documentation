---
 title: 'Autoruns'
---


{{< callout type="important" >}}Data Type: **autoruns** \
	Python Parser: **Autoruns**{{< /callout >}}

### Description 

Each row is an auto-start entry from a Sysinternals Autoruns CSV snapshot, with persistence location, entry name, enabled state, launch command, image path, profile, signer, and hashes. Use it to identify persistence candidates and correlate configured commands with files and users. Configuration at collection time does not prove the entry executed, and signature metadata is not a trust verdict.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `entry`   |
|Additional Description    | `image_path`   |
|    | `enabled`   |
|    | `category`   |
|    | `profile`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `time` | Python |  | timestamp of the autorun entry |
| `entry_location` | String | KEY_PATH | registry key path where the autorun entry is stored |
| `entry_name` | String | KEY_NAME | name of the registry value representing the autorun entry |
| `enabled` | Bool |  | indicates whether the autorun entry is enabled (active) |
| `category` | String |  | category of the autorun (e.g., Logon, Services, Drivers) |
| `profile` | String |  | user profile associated with the autorun entry |
| `description` | String |  | human‑readable description of the autorun entry |
| `signer` | String |  | signer of the digital signature of the executable |
| `company` | String | COMPANY | company name embedded in the executable |
| `image_path` | String | FILE_PATH | full file‑system path of the executable or script |
| `version` | String | PE_VERSION | version information of the executable (PE version) |
| `launch_string` | String |  | command line or arguments used to launch the executable |
| `md5` | String | FILE_MD5 | MD5 hash of the executable file |
| `sha1` | String | FILE_SHA1 | SHA‑1 hash of the executable file |
| `pe_sha1` | String | PE_SHA1 | SHA‑1 hash of the PE header |
| `pe_sha256` | String | PE_SHA256 | SHA‑256 hash of the PE header |
| `sha256` | String | FILE_SHA256 | SHA‑256 hash of the executable file |
| `imp` | String |  | list of imported functions or DLLs used by the executable |
