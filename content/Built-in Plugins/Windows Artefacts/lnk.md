---
 title: 'Lnk'
---


{{< callout type="important" >}}Data Type: **lnk** \
	Python Parser: **LnkBatched**{{< /callout >}}

### Description 

Each row describes a Windows Shell Link or Jump List shortcut, preserving target paths, arguments, working directory, target metadata, volume and tracker identifiers, link flags, and extra data. Use it to infer access or launch context and correlate files, devices, shares, and hosts, but shortcut creation alone does not prove the target was opened. Local DOS or FAT times are normalized with the matching SYSTEM hive; header FILETIME values remain unchanged.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `link_info.local_base_path`   |
|Additional Description    | `header.file_size`   |
|    | `header.windowstyle`   |
|    | `header.link_flags`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `file_creation_date` | DateTime | file creation date |
| `file_modif_date` | DateTime | file modification date |
| `type` | String | Type of the shell link record |
| `status` | String | Parsing status of the .lnk record |
| `size` | Int | Size of the .lnk record in bytes |
| `modification_time` | DateTime | Modification time of the .lnk file |
| `header` | Object |  |
| `header.guid` | StringToLower | LinkCLSID: class identifier (CLSID). This value MUST be {00021401-0000-0000-C000-000000000046} |
| `header.link_flags[]` | Array[String] | LinkFlags: specifies information about the shell link and the presence of optional portions of the structure |
| `header.file_flags[]` | Array[String] | FileAttributes: specifies information about the link target. |
| `header.creation_time` | DateTime | Specifies the creation time of the link target in UTC (Coordinated Universal Time). If the value is zero, there is no creation time set on the link target. |
| `header.access_time` | DateTime | Specifies the access time of the link target in UTC (Coordinated Universal Time). If the value is zero, there is no access time set on the link target. |
| `header.modification_time` | DateTime | Specifies the write time of the link target in UTC (Coordinated Universal Time). If the value is zero, there is no write time set on the link target. |
| `header.file_size` | Int | Specifies the size, in bytes, of the link target. If the link target file is larger than 0xFFFFFFFF, this value specifies the least significant 32 bits of the link target file size. |
| `header.icon_index` | Int | Specifies the index of an icon within a given icon location |
| `header.windowstyle` | String | ShowCommand: specifies the expected window state of an application launched by the link. |
| `header.hotkey` | String | Specifies the keystrokes used to launch the application referenced by the shortcut key. This value is assigned to the application after it is launched, so that pressing the key activates that application. |
| `header.reserved0` | Int | A value that MUST be zero |
| `header.reserved1` | Int | A value that MUST be zero |
| `header.reserved2` | Int | A value that MUST be zero |
| `data` | Object |  |
| `data.size` | Int | Size of the link data block in bytes |
| `data.description` | String | NAME_STRING specifies a description of the shortcut that is displayed to end users to identify the purpose of the shell link. |
| `data.relative_path` | String | RELATIVE_PATH specifies the location of the link target relative to the file that contains the shell link. When specified, this string SHOULD be used when resolving the link. |
| `data.working_directory` | String | WORKING_DIR specifies the file system path of the working directory to be used when activating the link target. |
| `data.command_line_arguments` | String | COMMAND_LINE_ARGUMENTS stores the command-line arguments that are specified when activating the link target. |
| `data.icon_location` | String | ICON_LOCATION specifies the location of the icon to be used when displaying a shell link item in an icon view. |
| `extra` | Object |  |
| `extra.console_codepage` | Int | Unsigned integer that specifies a code page language code identifier. |
| `extra.icon_location` | Object | Specifies the path to an icon. The path is encoded using environment variables, which makes it possible to find the icon across machines where the locations vary but are expressed using environment variables. |
| `extra.icon_location.size` | Int | Size of the icon location data block |
| `extra.icon_location.target_ansi` | String | Defined by the system default code page, which specifies a path to environment variable information. |
| `extra.icon_location.target_unicode` | String | Unicode string that specifies a path to environment variable information. |
| `extra.environmental_variables_location` | Object | Specifies a path to environment variable information when the link target refers to a location that has a corresponding environment variable. |
| `extra.environmental_variables_location.size` | Int | Size of the environment variables data block |
| `extra.environmental_variables_location.target_ansi` | String | Defined by the system default code page, which specifies a path to environment variable information. |
| `extra.environmental_variables_location.target_unicode` | String | Unicode string that specifies a path to environment variable information. |
| `extra.darwin_properties` | Object | Specifies an application identifier that can be used instead of a link target IDList to install an application when a shell link is activated. |
| `extra.darwin_properties.darwin_data_ansi` | String | defined by the system default code page, which specifies an application identifier. This field SHOULD be ignored. |
| `extra.darwin_properties.darwin_data_unicode` | String | Unicode string that specifies an application identifier. |
| `extra.darwin_properties.product_code_id` | StringToLower | Product code (GUID) of the MSI product |
| `extra.darwin_properties.feature_name` | String | Feature name of the MSI product |
| `extra.darwin_properties.component_id` | String | Component identifier of the MSI product |
| `extra.special_folder_location` | Object | Specifies the location of a special folder. This data can be used when a link target is a special folder to keep track of the folder, so that the link target IDList can be translated when the link is loaded. |
| `extra.special_folder_location.special_folder_id` | Int | Unsigned integer that specifies the folder integer ID. |
| `extra.special_folder_location.special_folder_name` | String | Translation of the special_folder_id value. |
| `extra.known_folder_location` | Object | Specifies the location of a known folder. This data can be used when a link target is a known folder to keep track of the folder so that the link target IDList can be translated when the link is loaded. |
| `extra.known_folder_location.known_folder_id` | StringToLower | GUID packet representation that specifies the folder GUID ID. |
| `extra.metadata_properties` | Object | PropertyStoreDataBlock specifies a set of properties that can be used by applications to store extra data in the shell link. |
| `extra.metadata_properties.size` | Int | Size of the metadata properties data block |
| `extra.metadata_properties.property_store[]` | Array[Object] | A serialized property storage structure |
| `extra.metadata_properties.property_store[].version` | String | Has to be equal to 0x53505331. |
| `extra.metadata_properties.property_store[].format_id` | StringToLower | A GUID that specifies the semantics and expected usage of the properties contained in this Serialized Property Storage structure. It MUST be unique in the set of serialized property storage structures. |
| `extra.metadata_properties.property_store[].serialized_property_values[]` | Array[Object] |  |
| `extra.metadata_properties.property_store[].serialized_property_values[].value_type` | String | Type identifier of the property value |
| `extra.metadata_properties.property_store[].serialized_property_values[].value` | Dynamic | Decoded serialized property value |
| `extra.metadata_properties.property_store[].serialized_property_values[].id` | Int | Property identifier |
| `extra.metadata_properties.property_store[].serialized_property_values[].name` | String | Property name |
| `extra.metadata_properties.property_store[].serialized_property_values[].name_size` | Int | Length of the property name string |
| `extra.shim_layer_properties` | Object | Specifies the name of a shim that can be applied when activating a link target. |
| `extra.shim_layer_properties.name` | String | LayerName: unicode string that specifies the name of a shim layer to apply to a link target when it is being activated |
| `extra.distributed_link_tracker` | Object | Specifies data that can be used to resolve a link target if it is not found in its original location when the link is resolved. This data is passed to the Link Tracking service to find the link target. |
| `extra.distributed_link_tracker.version` | String | This value MUST be 0x00000000. |
| `extra.distributed_link_tracker.machine_identifier` | String | Specifies the NetBIOS name of the machine where the link target was last known to reside. |
| `extra.distributed_link_tracker.droid_volume_identifier` | StringToLower | GUID volume identifier used by link tracking to locate the target |
| `extra.distributed_link_tracker.droid_file_identifier` | StringToLower | GUID file identifier used by link tracking to locate the target |
| `extra.distributed_link_tracker.droid_file_mft_seq` | Int | MFT sequence number of the target file |
| `extra.distributed_link_tracker.droid_file_frn` | IntToHex | Target file FRN (droid file identifier) as hexadecimal |
| `extra.distributed_link_tracker.droid_file_sequence_number` | Int | Sequence number of the target file MFT record |
| `extra.distributed_link_tracker.droid_file_record_number` | Int | Record number of the target file MFT entry |
| `extra.distributed_link_tracker.droid_file_mft_seq` | Extension | Target file FRN split into record and sequence number components |
| `extra.distributed_link_tracker.droid_file_frn_hex` | Int | Target file FRN (droid file identifier) as hexadecimal |
| `extra.distributed_link_tracker.droid_file_frn_split` | String | Target file FRN as record/sequence string |
| `extra.distributed_link_tracker.droid_file_timestamp` | DateTime | Timestamp resolved by the parser from the droid volume and file identifiers |
| `extra.distributed_link_tracker.droid_file_mac` | String | MAC address resolved by the parser from the droid volume and file identifiers |
| `extra.distributed_link_tracker.droid_file_vendor` | String | Vendor resolved by the parser from the droid volume and file identifiers |
| `extra.distributed_link_tracker.birth_droid_volume_identifier` | StringToLower | GUID volume identifier of the original (birth) file for link tracking |
| `extra.distributed_link_tracker.birth_droid_file_identifier` | StringToLower | GUID file identifier of the original (birth) file for link tracking |
| `extra.distributed_link_tracker.birth_droid_file_mft_seq` | Int | MFT sequence number of the birth (original) file |
| `extra.distributed_link_tracker.birth_droid_file_frn` | IntToHex | Birth (original) file FRN as hexadecimal |
| `extra.distributed_link_tracker.birth_droid_file_sequence_number` | Int | Sequence number of the birth (original) file MFT record |
| `extra.distributed_link_tracker.birth_droid_file_record_number` | Int | Record number of the birth (original) file MFT entry |
| `extra.distributed_link_tracker.birth_droid_file_mft_seq` | Extension | Birth (original) file FRN split into record and sequence components |
| `extra.distributed_link_tracker.birth_droid_file_timestamp` | DateTime | Timestamp resolved by the parser from the birth droid identifiers |
| `extra.distributed_link_tracker.birth_droid_file_mac` | String | MAC address resolved by the parser from the birth droid identifiers |
| `extra.distributed_link_tracker.birth_droid_file_vendor` | String | Vendor resolved by the parser from the birth droid identifiers |
| `extra.console_properties` | Object | Specifies the display settings to use when a link target specifies an application that is run in a console window. |
| `extra.console_properties.size` | Int | Size of the console properties data block |
| `extra.console_properties.fill_attributes` | Int | Specifies the fill attributes that control the foreground and background text colors in the console window. |
| `extra.console_properties.popup_fill_attributes` | Int | specifies the fill attributes that control the foreground and background text color in the console window popup. The values are the same as for the FillAttributes field. |
| `extra.console_properties.screen_buffer_size_x` | Int | Specifies the horizontal size (X axis), in characters, of the console window buffer. |
| `extra.console_properties.screen_buffer_size_y` | Int | Specifies the vertical size (Y axis), in characters, of the console window buffer. |
| `extra.console_properties.window_size_x` | Int | Specifies the horizontal size (X axis), in characters, of the console window. |
| `extra.console_properties.window_size_y` | Int | Specifies the vertical size (Y axis), in characters, of the console window. |
| `extra.console_properties.window_origin_x` | Int | Specifies the horizontal coordinate (X axis), in pixels, of the console window origin. |
| `extra.console_properties.window_origin_y` | Int | Specifies the vertical coordinate (Y axis), in pixels, of the console window origin. |
| `extra.console_properties.font_size` | Int | Specifies the size, in pixels, of the font used in the console window. |
| `extra.console_properties.font_family` | Int | Specifies the family of the font used in the console window. This value MUST be comprised of a font family and a font pitch. See the documentation table for interpretation. |
| `extra.console_properties.font_weight` | Int | Specifies the stroke weight of the font used in the console window. lower than 700: regular, greater than 700: bold. |
| `extra.console_properties.face_name` | String | Specifies the face name of the font used in the console window |
| `extra.console_properties.cursor_size` | Int | Specifies the size of the cursor, in pixels, used in the console window. lower than 25: small, 25-50: normal, 51-100: large. |
| `extra.console_properties.full_screen` | Int | Specifies whether to open the console window in full-screen mode. 0: windows, other: fullscreen. |
| `extra.console_properties.quick_edit` | Int | Specifies whether to open the console window in QuikEdit mode. In QuickEdit mode, the mouse can be used to cut, copy, and paste text in the console window. 0: off, other: on. |
| `extra.console_properties.insert_mode` | Int | Specifies insert mode in the console window. 0: disabled, other: enabled. |
| `extra.console_properties.auto_position` | Int | Specifies auto-position mode of the console window. 0: false, other: true ; if false, origin x and y are used. |
| `extra.console_properties.history_buffer_size` | Int | Specifies the size, in characters, of the buffer that is used to store a history of user input into the console window. |
| `extra.console_properties.number_of_history_buffers` | Int | Specifies the number of history buffers to use. |
| `extra.console_properties.history_no_dup` | Int | Specifies whether to remove duplicates in the history buffer. 0: duplicates not allowed, other: duplicates allowed |
| `extra.console_properties.color_table` | Int | specifying the RGB colors that are used for text in the console window. The values of the fill attribute fields FillAttributes and PopupFillAttributes are used as indexes into this table to specify the final foreground and background color for a character. |
| `extra.shell_item_identifier` | Object | The VistaAndAboveIDListDataBlock structure specifies an alternate IDList that can be used instead of the LinkTargetIDList structure on platforms that support it. |
| `extra.shell_item_identifier.id_list[]` | Array[Object] | An IDList structure |
| `extra.terminal_properties` | Object | A structure that indicates the end of the extra data section. |
| `extra.terminal_properties.size` | Int | Size of the terminal block |
| `extra.terminal_properties.appended_data_sha256` | String | SHA-256 of the appended data block |
| `extra.terminal_properties.appended_data_base64` | String | Appended data block as base64 |
| `target` | Object |  |
| `target.items[]` | Array[Object] |  |
| `target.items[].strings[]` | Array[String] | Strings extracted from identifiers by the in-house parser |
| `target.items[].identifiers` | Object | Identifiers of the shell item (item class and associated data) |
| `target.items[].item_class` | String | Common to every item types (RootFolder, VolumeItem, FileEntry, Internet, ControlPanel, UsersFilesFolder, Unknown). Indicates the type of element (Root Folder, Volume Item, File entry, etc...). |
| `target.items[].sort_index` | String | For items type 'RootFolder', should contains the root of the link. |
| `target.items[].guid` | StringToLower | For items type 'RootFolder', should contains a ShellFolderID. |
| `target.items[].class_type_indicator` | Int | Raw form (int) of flags; verify and hide if correct |
| `target.items[].flags` | String | For items type 'VolumeItem' and 'FileEntry', contains a flag, possibly as a string if interpreted by the parser (examples: Is directory, Is file) and an int/hex value otherwise. |
| `target.items[].data` | String | For items type 'VolumeItem', should contain the volume letter. |
| `target.items[].size` | Int | For items type 'FileEntry', contains the size of the target file (and probably 0 for a directory). |
| `target.items[].modification_time` | DateTime | For FileEntry items, UTC last-modification timestamp converted from the embedded DOS/FAT local time using the matching SYSTEM hive |
| `target.items[].file_attribute_flags` | Int | Target file attribute flags (for FileEntry items) |
| `target.items[].primary_name` | String | For items type 'FileEntry', name of a file or directory in the target path. |
| `target.items[].item_identifier` | String | For items type 'ControlPanel' |
| `target.items[].data_base64` | String | Base64 content for Unknown item_class values. |
| `target.items[].data_sha256` | String | SHA-256 of the content for Unknown item_class values. |
| `target.target_path` | String | Full path of the link target |
| `link_info` | Object |  |
| `link_info.local_base_path` | String | Local base path of the target from the LinkInfo |
| `link_info.common_path_suffix` | String | Common path suffix appended to the base path |
| `link_info.location` | String | Location of the link target (drive or UNC) |
| `link_info.location_info` | Object |  |
| `link_info.location_info.r_drive_type` | Int | Raw drive type value (e.g., DRIVE_FIXED) |
| `link_info.location_info.drive_type` | String | Drive type of the link target's volume |
| `link_info.location_info.drive_serial_number` | String | Serial number of the link target volume |
| `link_info.location_info.volume_label` | String | Volume label of the link target volume |
| `link_info.location_info.volume_label_unicode` | String | Volume label of the link target volume (Unicode) |
| `link_info.location_info.common_network_relative_link_flags` | String | Flags of the CommonNetworkRelativeLink structure |
| `link_info.location_info.r_network_provider_type` | String | Raw network provider type value |
| `link_info.location_info.network_provider_type` | String | Network provider type of the link target |
| `link_info.location_info.net_name` | String | UNC network path of the link target |
| `link_info.location_info.net_name_unicode` | String | UNC network path of the link target (Unicode) |
| `link_info.location_info.device_name` | String | Device/computer name of the link target on the network |
| `link_info.location_info.device_name_unicode` | String | Device/computer name of the link target (Unicode) |
| `slack` | Object |  |
| `slack.payload` | String | Payload bytes recovered from slack or extra space |
