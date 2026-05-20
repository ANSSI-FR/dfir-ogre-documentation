---
 title: 'Tcpvcon'
---


{{< callout type="important" >}}Data Type: **tcpvcon** \
	Python Parser: **TCPConn**{{< /callout >}}

### Description 

Parse a TCPView “Tcpvcon.txt” export.


### Timeline 

{{< callout type="warning" >}}This plugin does not contains timestamped data and cannot be used to create a timeline{{< /callout >}}
### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `process_name` | String |  | Process name |
| `pid` | String |  | PID |
| `protocol` | String |  | Protocol.  e.g. TCP, UDP, TCPV6, UDPV6 |
| `state` | String |  | LISTENING, ESTABLISHED, … (can be empty for UDP) |
| `local_adress` | String |  | local addres |
| `remote_adress` | String |  | remote address |
