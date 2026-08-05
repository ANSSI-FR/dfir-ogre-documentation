---
 title: 'Mass Storage'
---


{{< callout type="important" >}}Data Type: **mass_storage** \
	Python Parser: **RegMassStorageSystem**{{< /callout >}}

### Description 

Each row consolidates registry evidence for a mass-storage device, with device and instance identifiers, serial or volume labels, drive mapping, user context, and setup or arrival/removal times where available. Use it to correlate removable media across registry sources and file activity. Timestamps have source-specific meanings and should be corroborated before inferring an exact physical connection.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `users`   |
|Description    | `type`   |
|    | `vendor`   |
|    | `product`   |
|    | `instance_id`   |
|Additional Description    | `class_id`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `class_id` | String | class identifier of the device (e.g., USBSTOR class ID) |
| `friendly_names[]` | Array[String] | list of friendly display names for the device |
| `controlset` | String | registry control set (e.g., ControlSet001) where the device information resides |
| `parent_id` | String | parent identifier linking to a related device entry |
| `volume_guid` | String | GUID of the volume associated with the device |
| `driver` | String | driver name or path handling the device |
| `type` | String | type of the device |
| `vendor` | String | vendor name extracted from the device class ID |
| `product` | String | product name extracted from the device class ID |
| `instance_id` | String | unique instance ID of the device |
| `revision` | String | hardware revision of the device |
| `silo` | String | silo/segment identifier for the device |
| `vendor_id` | String | USB vendor ID (VID) |
| `product_id` | String | USB product ID (PID) |
| `volume_letter` | String | assigned drive letter (e.g., C:) |
| `volume_label` | String | label of the volume |
| `volume_sn` | String | serial number of the volume |
| `capacity` | String | storage capacity of the volume |
| `attributes1` | String | raw attribute string 1 from device metadata |
| `attributes2` | String | raw attribute string 2 from device metadata |
| `attributes3` | String | raw attribute string 3 from device metadata |
| `reason` | String | reason string associated with device install or removal events |
| `registry_path` | String | registry key paths that contributed to this device record |
| `setupapi_sample_path` | String | path to the SetupAPI sample file used for this record |
| `users` | String | owner SID(s) of the registry entries |
| `setupapi_first_seen` | DateTime | first timestamp the device appeared in SetupAPI (installation) |
| `setupapi_last_seen` | DateTime | last timestamp the device appeared in SetupAPI (removal) |
| `usbstor_last_modified` | DateTime | last modification timestamp of the USBSTOR registry key |
| `device_classes_last_modified` | DateTime | last modification timestamp of the DeviceClasses registry key |
| `usb_last_modified` | DateTime | last modification timestamp of the USB enumeration key |
| `emdmgmt_last_modified` | DateTime | last modification timestamp of the EMDMGMT registry key |
| `usbstor_first_install` | DateTime | first install timestamp from USBSTOR properties |
| `usbstor_install` | DateTime | install timestamp of the USBSTOR device |
| `usbstor_last_arrival` | DateTime | timestamp of the most recent device arrival |
| `usbstor_last_removal` | DateTime | timestamp of the most recent device removal |
