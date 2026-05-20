---
 title: 'Wer'
---


{{< callout type="important" >}}Data Type: **wer** \
	Python Parser: **WER**{{< /callout >}}

### Description 

ParsesWindows Error Reporting files (WER), extracting metadata about crashes,
      hangs, and other failure events reported by the operating system.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `app_path`   |
|Additional Description    | `event_type`   |
|    | `original_file_name`   |
|    | `ns_app_name`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `version` | Int |  | Version of the Windows Error Reporting file format |
| `event_type` | String |  | Type of event that generated the report (e.g., crash, hang) |
| `event_time` | DateTime |  | Timestamp when the event occurred |
| `report_type` | Int |  | Numeric identifier of the report category |
| `consent` | Int |  | User‑provided consent flag for sending the report |
| `upload_time` | DateTime |  | Timestamp when the report was uploaded to Microsoft |
| `report_status` | Int |  | Current processing status of the report |
| `boot_id` | String |  | Identifier of the boot session during which the event happened |
| `target_as_id` | String |  | Identifier of the target application session |
| `user_impact_vector` | Int |  | Severity/impact rating of the failure event |
| `etw_non_collect_reason` | Int |  | Reason code why ETW data was not collected |
| `metadata_hash` | String |  | Hash of the report metadata for integrity verification |
| `application_identity` | String |  | Unique identifier of the reported application |
| `report_identifier` | String |  | Globally unique identifier for this WER report |
| `wow64_host` | String |  | Indicates if the report originated from a WoW64 (32‑bit on 64‑bit) process |
| `ns_app_name` | String |  | Namespace‑scoped name of the application |
| `original_filename` | String |  | Original file name of the crashed executable |
| `app_session_guid` | String |  | GUID of the application session that generated the report |
| `target_app_id` | String |  | Identifier of the target application |
| `target_app_ver` | String |  | Version of the target application |
| `app_path` | String |  | Full file‑system path to the application executable |
| `app_name` | String |  | Human‑readable name of the application |
| `is_fatal` | String |  | Flag indicating whether the failure was fatal |
| `friendly_event_name` | String |  | User‑friendly description of the event type |
| `consent_key` | String |  | Registry or configuration key associated with user consent |
| `report_description` | String |  | Textual description supplied with the report |
| `ns_partner` | String |  | Namespace partner identifier related to the application |
| `ns_group` | String |  | Namespace group identifier related to the application |
| `response_bucket_id` | String |  | Identifier of the bucket used for response classification |
| `response_bucket_table` | String |  | Name of the bucket table associated with the response |
| `response_legacy_bucket_id` | String |  | Legacy bucket identifier for backward‑compatible processing |
| `response_type` | String |  | Type/category of the response generated for the report |
| `loaded_module[]` | Array[String] |  | Name of a module that was loaded in the process at crash time |
| `files[]` | Array[Object] |  |  |
| `files[].CabName` | String |  | Name of the cabinet file containing the crash artifacts |
| `files[].Path` | String |  | File system path of the reported file |
| `files[].Flags` | String |  | Flags describing properties of the file |
| `files[].Type` | String |  | File type/category (e.g., dump, log, cab) |
| `files[].Original` | String |  | Original filename before it was packaged |
| `sig` | Object |  |  |
| `sig.os_version` | String |  | Operating‑system version recorded in the static signature |
| `sig.locale_id` | String |  | Locale identifier (LCID) of the system at the time of the crash |
| `dynamic_sig` | Object |  |  |
| `dynamic_sig.stack_version` | String |  | Version of the stack information included in the dynamic signature |
| `dynamic_sig.package` | String |  | Package name associated with the dynamic signature |
| `dynamic_sig.version` | String |  | Version of the package referenced in the dynamic signature |
| `dynamic_sig.architecture` | String |  | CPU architecture (e.g., x86, x64) reported in the dynamic signature |
| `dynamic_sig.culture` | String |  | Culture/language code of the package |
| `dynamic_sig.status` | String |  | Status flag of the dynamic signature |
| `dynamic_sig.failure_source` | String |  | Source component that caused the failure |
| `dynamic_sig.start_state` | String |  | Application state before the failure occurred |
| `dynamic_sig.target_state` | String |  | Application state targeted after the failure |
| `dynamic_sig.client_id` | String |  | Identifier of the client that generated the dynamic signature |
| `os_info` | Object |  |  |
| `state` | Object |  |  |
