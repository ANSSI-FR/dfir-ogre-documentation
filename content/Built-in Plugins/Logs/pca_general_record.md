---
 title: 'Pca General Record'
---


{{< callout type="important" >}}Data Type: **pca_general_record** \
	Python Parser: **Regexp**{{< /callout >}}

### Description 

Extracts each line of a PCA log. It captures when a program was launched, its status, executable location and associated metadata such as description, vendor, version, and exit code.

- Reveals the exact time a program was started.
- Provides the executable’s full path for correlation with other artefacts.
- Includes human‑readable file description, vendor and version for context.
- Records the run status and exit code, useful for success/failure determination.


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
