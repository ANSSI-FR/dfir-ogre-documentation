---
 title: 'Tcp Connections'
---


{{< callout type="important" >}}Data Type: **tcpvcon** \
	Python Parser: **TCPConn**{{< /callout >}}

### Description 

Each row is a TCP or UDP endpoint from a Sysinternals Tcpvcon snapshot, with owning process and identifier, protocol and state, and local or remote addresses and ports. Use it to correlate collection-time network exposure with processes and other telemetry. It contains no payload or connection history, and process attribution can become stale as identifiers are reused.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `process_name`   |
|    | `protocol`   |
|Additional Description    | `state`   |
|    | `local_adress`   |
|    | `remote_adress`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `process_name` | String |  | Process name |
| `pid` | String |  | PID |
| `protocol` | String |  | Protocol.  e.g. TCP, UDP, TCPV6, UDPV6 |
| `state` | String |  | LISTENING, ESTABLISHED, … (can be empty for UDP) |
| `local_adress` | String |  | local addres |
| `remote_adress` | String |  | remote address |
