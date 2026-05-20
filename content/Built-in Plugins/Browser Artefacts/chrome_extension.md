---
 title: 'Chrome Extension'
---


{{< callout type="important" >}}Data Type: **chrome_extension** \
	Python Parser: **ChromeExtension**{{< /callout >}}

### Description 

Extracts metadata from a Chrome‑based browser extension’s manifest. It reads fields such as
name, version, description, update URL, permissions and optional permissions, providing a
structured view of the extension’s declared capabilities.

- Identifies the extension’s displayed name and version.
- Lists required, host and optional permissions, revealing potential system interactions.
- Captures localisation, description and update URL for contextual information.


### Timeline 

{{< callout type="warning" >}}This plugin does not contains timestamped data and cannot be used to create a timeline{{< /callout >}}
### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `name` | String |  | display name of the Chrome extension |
| `version` | String |  | version of the extension |
| `default_locale` | String |  | default locale identifier for the extension's resources |
| `description` | String |  | human‑readable description of the extension |
| `update_url` | String |  | URL from which the extension receives updates |
| `extension_pages` | String |  | CSP‑allowed pages that may be opened by the extension |
| `permissions[]` | Array[String] |  | required permissions declared by the extension |
| `host_permissions[]` | Array[String] |  | host (URL) permissions declared by the extension |
| `optional_permissions[]` | Array[String] |  | optional permissions that can be granted by the user |
