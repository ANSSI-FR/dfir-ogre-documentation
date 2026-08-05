---
 title: 'Pca General Record'
---


{{< callout type="important" >}}Data Type: **pca_general_record** \
	Python Parser: **Regexp**{{< /callout >}}

### Description 

Each row is a Program Compatibility Assistant general record, with run time, executable path, status, vendor, version, program identifier, and exit code where available. Use it to support execution analysis and correlate compatibility handling with binaries and other timelines. Status and exit code describe the recorded PCA interaction and should not alone be treated as the program's full outcome.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `executable_path`   |
|Additional Description    | `file_description`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `run_time` | DateTime | DATE_LAST_RUN | timestamp when the program was launched |
| `run_status` | Int |  | numeric run status (e.g., 0 = success, non‑zero = error) |
| `executable_path` | String | FILE_PATH | full path of the executable launched via PCA |
| `file_description` | String |  | human‑readable description of the executable or program |
| `software_vendor` | String | PUBLISHER | name of the software vendor or publisher |
| `file_version` | String |  | version of the executable |
| `program_id` | String | APP_ID | unique identifier for the program |
| `exitcode_value` | String | EXIT_CODE | exit code returned by the program after execution |
