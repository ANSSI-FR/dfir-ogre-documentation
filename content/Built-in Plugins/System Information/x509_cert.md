---
 title: 'X509 Cert'
---


{{< callout type="important" >}}Data Type: **x509_cert** \
	Python Parser: **RegSystemCertificates**{{< /callout >}}

### Description 

Parses the Windows `Software` registry hive to collect system‑wide X509 certificates stored in the `Software` hive. It reads the binary certificate blobs, decodes them, and extracts key certificate attributes.

- Provides complete certificate details (subject, issuer, validity period, public‑key algorithm, fingerprint).


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `subject`   |
|Additional Description    | `issuer`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `subject` | String |  | certificate subject distinguished name (RFC 4514 format) |
| `issuer` | String |  | certificate issuer distinguished name (RFC 4514 format) |
| `not_valid_before` | DateTime |  | certificate start‑of‑validity timestamp (not before) |
| `not_valid_after` | DateTime |  | certificate end‑of‑validity timestamp (not after) |
| `pub_key_algo` | String |  | public‑key algorithm name (e.g., rsaEncryption) |
| `pub_key_algo_oid` | String |  | OID of the public‑key algorithm |
| `fingerprint_sha256` | String |  | SHA‑256 fingerprint of the certificate (hex string) |
| `version` | String |  | X.509 certificate version |
| `serial_number` | String |  | certificate serial number (decimal string) |
| `extensions[]` | Array[Object] |  |  |
| `extensions[].name` | String |  | human‑readable name of the extension |
| `extensions[].oid` | String |  | object identifier (OID) of the extension |
| `extensions[].critical` | String |  | whether the extension is marked critical (true/false) |
| `extensions[].value` | String |  | string representation of the extension value |
| `key_path` | String | KEY_PATH | full registry key name |
| `key_modif_time` | DateTime | DATE_MODIFICATION | last modification timestamp of the registry key |
| `key_security` | Object |  |  |
| `key_security.owner_sid` | String | USER_SID | SID of the user that owns the registry key |
| `key_security.group_sid` | String |  | SID of the group that owns the registry key |
| `key_security.control_flags[]` | Array[String] |  | security descriptor control flags for the key |
| `key_security.sacl_aces[]` | Array[Object] |  |  |
| `key_security.sacl_aces[].ace_type` | String |  | type of ACE (e.g., allow, deny) |
| `key_security.sacl_aces[].ace_flags[]` | Array[String] |  | ACE flags that modify inheritance or behavior |
| `key_security.sacl_aces[].rights[]` | Array[String] |  | permissions granted or denied by the ACE |
| `key_security.sacl_aces[].account_sid` | String |  | SID of the account the ACE applies to |
| `key_security.sacl_aces[].ace_size` | Int |  | declared ACE size in bytes |
| `key_security.sacl_aces[].object_type_guid` | String |  | GUID identifying the object type governed by the ACE |
| `key_security.sacl_aces[].inherited_object_type_guid` | String |  | GUID identifying the inherited object type governed by the ACE |
| `key_security.sacl_aces[].raw_hex` | String |  | raw ACE bytes preserved as hexadecimal |
| `key_security.dacl_aces[]` | Array[Object] |  |  |
| `key_security.dacl_aces[].ace_type` | String |  | type of ACE (e.g., allow, deny) |
| `key_security.dacl_aces[].ace_flags[]` | Array[String] |  | ACE flags that modify inheritance or behavior |
| `key_security.dacl_aces[].rights[]` | Array[String] |  | permissions granted or denied by the ACE |
| `key_security.dacl_aces[].account_sid` | String |  | SID of the account the ACE applies to |
| `key_security.dacl_aces[].ace_size` | Int |  | declared ACE size in bytes |
| `key_security.dacl_aces[].object_type_guid` | String |  | GUID identifying the object type governed by the ACE |
| `key_security.dacl_aces[].inherited_object_type_guid` | String |  | GUID identifying the inherited object type governed by the ACE |
| `key_security.dacl_aces[].raw_hex` | String |  | raw ACE bytes preserved as hexadecimal |
