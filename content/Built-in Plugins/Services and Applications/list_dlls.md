---
 title: 'List Dlls'
---


{{< callout type="important" >}}Data Type: **listdlls** \
	Python Parser: **ListDll**{{< /callout >}}

### Description 

Each row is a module listed by Sysinternals ListDLLs for a process observed at collection time, with process name, identifier, command line, module path, base address, and size. Use it to detect unexpected DLL loads and correlate modules with processes and hashes from other artifacts. It is a transient snapshot; absent or terminated processes are not represented and process identifiers can be reused.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `path`   |
|Additional Description    | `process_name`   |
|    | `pid`   |
|    | `base_addr`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `process_name` | String |  | Process name |
| `pid` | String |  | PID |
| `command_line` | String |  | Full command line used to start the process |
| `base_addr` | String |  | Base address in memory where the DLL is loaded (hexadecimal) |
| `size` | String |  | Size of the DLL module in memory  |
| `path` | String |  |  Full path to the DLL file on disk |
