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

| Output Name | Data Type | Description |
|---|---|---|
| `time` | Python | timestamp of the autorun entry |
| `entry_location` | String | registry key path where the autorun entry is stored |
| `entry_name` | String | name of the registry value representing the autorun entry |
| `enabled` | Bool | indicates whether the autorun entry is enabled (active) |
| `category` | String | category of the autorun (e.g., Logon, Services, Drivers) |
| `profile` | String | user profile associated with the autorun entry |
| `description` | String | human‑readable description of the autorun entry |
| `signer` | String | signer of the digital signature of the executable |
| `company` | String | company name embedded in the executable |
| `image_path` | String | full file‑system path of the executable or script |
| `version` | String | version information of the executable (PE version) |
| `launch_string` | String | command line or arguments used to launch the executable |
| `md5` | String | MD5 hash of the executable file |
| `sha1` | String | SHA‑1 hash of the executable file |
| `pe_sha1` | String | SHA‑1 hash of the PE header |
| `pe_sha256` | String | SHA‑256 hash of the PE header |
| `sha256` | String | SHA‑256 hash of the executable file |
| `imp` | String | list of imported functions or DLLs used by the executable |
