---
 title: 'Processes Orc'
---


{{< callout type="important" >}}Data Type: **processes_orc** \
	Python Parser: **OrcProcesses1**{{< /callout >}}

### Description 

Extracts Windows processes data from an ORC‑generated CSV file. It captures basic process attributes such as name, executable path, command line, identifiers and timestamps, exposing the execution context recorded at collection time.

- Provides process names and their originating executable locations.
- Records command‑line arguments, enabling reconstruction of launch parameters.
- Includes creation and termination timestamps for temporal correlation.
- Supplies process IDs, parent IDs and session information for relationship mapping.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `name`   |
|Additional Description    | `command_line`   |
|    | `executable_path`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `name` | String |  | name of the process executable |
| `nb_handles` | Int |  | number of handles opened by the process |
| `executable_path` | String |  | full file‑system path to the process executable |
| `command_line` | String | COMMAND_LINE | command‑line used to launch the process |
| `description` | String |  | human‑readable description of the process |
| `creation` | Python |  | timestamp when the process was created |
| `termination` | Python |  | timestamp when the process terminated (if any) |
| `kernelmode_time` | String |  | cumulative CPU time spent in kernel mode |
| `usermode_time` | String |  | cumulative CPU time spent in user mode |
| `parent_id` | Int | PROCESS_ID | identifier of the parent process |
| `priority` | Int |  | process priority value |
| `process_id` | Int |  | identifier (PID) of the process |
| `session_id` | Int |  | session identifier to which the process belongs |
| `nb_threads` | Int |  | number of threads created by the process |
| `memory_size` | Int |  | virtual memory size allocated to the process (bytes) |
