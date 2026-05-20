---
 title: 'Listdlls'
---


{{< callout type="important" >}}Data Type: **listdlls** \
	Python Parser: **ListDll**{{< /callout >}}

### Description 

Parse output from Sysinternals **ListDLL** tool that lists loaded DLLs for running processes on Windows.


### Timeline 

{{< callout type="warning" >}}This plugin does not contains timestamped data and cannot be used to create a timeline{{< /callout >}}
### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `process_name` | String |  | Process name |
| `pid` | String |  | PID |
| `command_line` | String |  | Full command line used to start the process |
| `base_addr` | String |  | Base address in memory where the DLL is loaded (hexadecimal) |
| `size` | String |  | Size of the DLL module in memory  |
| `path` | String |  |  Full path to the DLL file on disk |
