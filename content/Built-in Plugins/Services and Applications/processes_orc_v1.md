---
 title: 'Processes Orc V1'
---


{{< callout type="important" >}}Data Type: **processes_orc** \
	Python Parser: **OrcProcesses1**{{< /callout >}}

### Description 

Each row describes a process observed in an ORC process CSV, with name, executable path, command line, process and parent identifiers, session, and creation or termination times. Use it to reconstruct process ancestry and correlate execution context with files, users, and network evidence. It is a collection-time view; absence does not exclude earlier execution and identifiers can be reused.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `name`   |
|Additional Description    | `command_line`   |
|    | `executable_path`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `name` | String | name of the process executable |
| `nb_handles` | Int | number of handles opened by the process |
| `executable_path` | String | full file‑system path to the process executable |
| `command_line` | String | command‑line used to launch the process |
| `description` | String | human‑readable description of the process |
| `creation` | Python | timestamp when the process was created |
| `termination` | Python | timestamp when the process terminated (if any) |
| `kernelmode_time` | String | cumulative CPU time spent in kernel mode |
| `usermode_time` | String | cumulative CPU time spent in user mode |
| `parent_id` | Int | identifier of the parent process |
| `priority` | Int | process priority value |
| `process_id` | Int | identifier (PID) of the process |
| `session_id` | Int | session identifier to which the process belongs |
| `nb_threads` | Int | number of threads created by the process |
| `memory_size` | Int | virtual memory size allocated to the process (bytes) |
