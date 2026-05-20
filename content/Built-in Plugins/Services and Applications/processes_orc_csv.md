---
 title: 'Processes Orc Csv'
---


{{< callout type="important" >}}Data Type: **processes_orc** \
	Python Parser: **Csv**{{< /callout >}}

### Description 

Parses CSV files produced by ORC that enumerate running processes. It extracts each process’s metadata, such as name, executable path, timestamps, identifiers, and resource usage.

- Process name, command‑line and executable location.
- Creation (`creation`) and termination (`termination`) timestamps.
- Parent/child relationship via `parent_id` and `process_id`.
- Resource metrics: memory size, CPU times, priority, session.
- Execution context: user‑mode/kernel‑mode time, responding state, privileged flag.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `name`   |
|Additional Description    | `command_line`   |
|    | `executable_path`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `name` | String |  | executable name of the process (without path) |
| `nb_handles` | Int |  | total number of handles opened by the process |
| `executable_path` | String |  | full filesystem path to the process executable |
| `company` | String | COMPANY | publisher name extracted from the executable's version info |
| `cpu_time` | String |  | cumulative CPU time consumed by the process |
| `file_version` | String |  | file version string from the executable's version resource |
| `product_version` | String |  | product version string from the executable's version resource |
| `product` | String | PRODUCT | product name extracted from the executable's version info |
| `window_title` | String |  | title of the process's main window, if present |
| `description` | String |  | human‑readable description from the executable's version info |
| `creation` | String |  | timestamp when the process was created |
| `termination` | String |  | timestamp when the process terminated (if applicable) |
| `kernelmode_time` | String |  | CPU time spent in kernel‑mode (privileged) for the process |
| `usermode_time` | String |  | CPU time spent in user‑mode for the process |
| `total_time` | String |  | total CPU time (user + kernel) consumed by the process |
| `parent_id` | Int | PROCESS_ID | process identifier (PID) of the parent process |
| `priority_class` | String |  | string representation of the process's priority class |
| `priority` | Int |  | numeric priority value of the process |
| `process_id` | Int |  | process identifier (PID) of the current process |
| `session_id` | Int |  | identifier of the session in which the process runs |
| `responding` | String |  | indicates whether the process is currently responding (True/False) |
| `memory_size` | Int |  | virtual memory size allocated to the process (in bytes) |
