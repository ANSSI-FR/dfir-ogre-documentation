---
 title: 'Processes Orc V2'
---


{{< callout type="important" >}}Data Type: **processes_orc** \
	Python Parser: **Csv**{{< /callout >}}

### Description 

Each row describes a process observed in an enriched ORC process CSV, with identity, executable and command line, parentage, timing, version, window, resource, and response metadata. Use it to reconstruct process trees and flag anomalous paths or behavior. It remains a snapshot; absence does not exclude earlier execution and identifiers can be reused.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `name`   |
|Additional Description    | `process_id`   |
|    | `executable_path`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `name` | String | executable name of the process (without path) |
| `nb_handles` | Int | total number of handles opened by the process |
| `executable_path` | String | full filesystem path to the process executable |
| `company` | String | publisher name extracted from the executable's version info |
| `cpu_time` | String | cumulative CPU time consumed by the process |
| `file_version` | String | file version string from the executable's version resource |
| `product_version` | String | product version string from the executable's version resource |
| `product` | String | product name extracted from the executable's version info |
| `window_title` | String | title of the process's main window, if present |
| `description` | String | human‑readable description from the executable's version info |
| `creation` | String | timestamp when the process was created |
| `termination` | String | timestamp when the process terminated (if applicable) |
| `kernelmode_time` | String | CPU time spent in kernel‑mode (privileged) for the process |
| `usermode_time` | String | CPU time spent in user‑mode for the process |
| `total_time` | String | total CPU time (user + kernel) consumed by the process |
| `parent_id` | Int | process identifier (PID) of the parent process |
| `priority_class` | String | string representation of the process's priority class |
| `priority` | Int | numeric priority value of the process |
| `process_id` | Int | process identifier (PID) of the current process |
| `session_id` | Int | identifier of the session in which the process runs |
| `responding` | String | indicates whether the process is currently responding (True/False) |
| `memory_size` | Int | virtual memory size allocated to the process (in bytes) |
