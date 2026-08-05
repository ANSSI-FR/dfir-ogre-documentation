---
 title: 'Chrome Extension'
---


{{< callout type="important" >}}Data Type: **chrome_extension** \
	Python Parser: **ChromeExtension**{{< /callout >}}

### Description 

Each row describes an installed Chrome extension manifest, including identity, version, source, update URL, declared permissions, content scripts, background code, accessible resources, and security policy. Use it to assess extension capability and provenance or hunt risky permissions and injected origins. Declared capability is not proof that code ran, and the snapshot can miss removed versions.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `name`   |
|    | `browser`   |
|Additional Description    | `extension_id`   |
|    | `version`   |
|    | `manifest_path`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `browser` | String |  | browser family that owns the extension manifest |
| `extension_id` | String |  | Chrome extension ID inferred from the standard Extensions directory path |
| `extension_type` | String |  | manifest type: extension, app or theme |
| `manifest_path` | String |  | filesystem path of the parsed manifest |
| `manifest_sha256` | String |  | SHA-256 hash of the parsed manifest file |
| `manifest_version` | Int |  | Chrome manifest format version |
| `version_directory` | String |  | installed extension version directory inferred from the manifest path |
| `name` | String |  | localized display name of the Chrome extension when available |
| `short_name` | String |  | short display name declared by the extension |
| `version` | String |  | extension version declared by the manifest |
| `version_name` | String |  | human-readable extension version label |
| `author` | String |  | extension author declared by the manifest |
| `default_locale` | String |  | default locale identifier for the extension's resources |
| `description` | String |  | localized human-readable extension description when available |
| `homepage_url` | String |  | homepage URL declared by the extension |
| `update_url` | String |  | URL from which the extension receives updates |
| `minimum_chrome_version` | String |  | oldest compatible Chrome version declared by the extension |
| `incognito` | String |  | declared incognito-mode behavior |
| `offline_enabled` | Bool |  | whether the extension declares offline operation |
| `extension_pages` | String |  | CSP for extension pages, including the complete Manifest V2 policy |
| `sandbox_pages` | String |  | Manifest V3 CSP for sandboxed extension pages |
| `background_service_worker` | String |  | Manifest V3 background service-worker script |
| `background_page` | String |  | Manifest V2 background page |
| `background_persistent` | Bool |  | whether a Manifest V2 background context is persistent |
| `background_scripts[]` | Array[String] |  | Manifest V2 background scripts |
| `permissions[]` | Array[String] |  | required permissions exactly as declared by the extension |
| `host_permissions[]` | Array[String] |  | normalized host access, including Manifest V2 permission URL patterns |
| `optional_permissions[]` | Array[String] |  | optional permissions exactly as declared by the extension |
| `optional_host_permissions[]` | Array[String] |  | normalized optional host access across Manifest V2 and V3 |
| `content_script_matches[]` | Array[String] |  | URL patterns on which extension content scripts execute |
| `content_script_exclude_matches[]` | Array[String] |  | URL patterns excluded from content-script execution |
| `content_script_javascript[]` | Array[String] |  | JavaScript files injected by content scripts |
| `content_script_stylesheets[]` | Array[String] |  | stylesheets injected by content scripts |
| `externally_connectable_matches[]` | Array[String] |  | web origins allowed to connect to the extension |
| `externally_connectable_ids[]` | Array[String] |  | other extension IDs allowed to connect to the extension |
| `web_accessible_resources[]` | Array[String] |  | extension resources exposed outside the extension |
| `web_accessible_matches[]` | Array[String] |  | Manifest V3 web origins allowed to access exposed resources |
| `web_accessible_extension_ids[]` | Array[String] |  | Manifest V3 extension IDs allowed to access exposed resources |
