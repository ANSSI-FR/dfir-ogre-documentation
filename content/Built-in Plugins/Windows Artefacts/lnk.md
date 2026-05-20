---
 title: 'Lnk'
---


{{< callout type="important" >}}Data Type: **lnk** \
	Python Parser: **LnkBatched**{{< /callout >}}

### Description 

Extracts every pieces of metadata that is stored in a Windows Shell Link file.
From a digital‑forensic perspective a shortcut can reveal:

- the **target path** that a user intended to open (file, folder, network share, or special folder).
- timestamps of the **target file** (creation, modification, access) and of the shortcut itself.
- **command‑line arguments, working directory, icon information, hot‑key, window style** – all useful for reconstructing the user’s workflow.
- **Link‑flags, file‑attributes, and extra data blocks** (e.g., Distributed Link Tracker, Shim layer, console properties) that can indicate the presence of shims, virtualisation, or relocation attempts.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `link_info.local_base_path`   |
|Additional Description    | `header.file_size`   |
|    | `header.windowstyle`   |
|    | `header.link_flags`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `file_creation_date` | DateTime | DATE_CREATION | file creation date |
| `file_modif_date` | DateTime | DATE_MODIFICATION | file modification date |
| `type` | String |  |  |
| `status` | String |  |  |
| `size` | Int |  |  |
| `modification_time` | DateTime |  |  |
| `header` | Object |  |  |
| `header.guid` | StringToLower |  | LinkCLSID: class identifier (CLSID). This value MUST be {00021401-0000-0000-C000-000000000046} |
| `header.link_flags[]` | Array[String] |  | LinkFlags: specifies information about the shell link and the presence of optional portions of the structure |
| `header.file_flags[]` | Array[String] |  | FileAttributes: specifies information about the link target. |
| `header.creation_time` | DateTime | DATE_CREATION | Specifies the creation time of the link target in UTC (Coordinated Universal Time). If the value is zero, there is no creation time set on the link target. |
| `header.access_time` | DateTime | DATE_ACCESS | Specifies the access time of the link target in UTC (Coordinated Universal Time). If the value is zero, there is no access time set on the link target. |
| `header.modification_time` | DateTime | DATE_MODIFICATION | Specifies the write time of the link target in UTC (Coordinated Universal Time). If the value is zero, there is no write time set on the link target. |
| `header.file_size` | Int | FILE_SIZE | Specifies the size, in bytes, of the link target. If the link target file is larger than 0xFFFFFFFF, this value specifies the least significant 32 bits of the link target file size. |
| `header.icon_index` | Int |  | Specifies the index of an icon within a given icon location |
| `header.windowstyle` | String |  | ShowCommand: specifies the expected window state of an application launched by the link. |
| `header.hotkey` | String |  | Specifies the keystrokes used to launch the application referenced by the shortcut key. This value is assigned to the application after it is launched, so that pressing the key activates that application. |
| `header.reserved0` | Int |  | A value that MUST be zero |
| `header.reserved1` | Int |  | A value that MUST be zero |
| `header.reserved2` | Int |  | A value that MUST be zero |
| `data` | Object |  |  |
| `data.size` | Int |  |  |
| `data.description` | String |  | NAME_STRING specifies a description of the shortcut that is displayed to end users to identify the purpose of the shell link. |
| `data.relative_path` | String | FILE_PATH | RELATIVE_PATH specifies the location of the link target relative to the file that contains the shell link. When specified, this string SHOULD be used when resolving the link. |
| `data.working_directory` | String | FILE_PATH | WORKING_DIR specifies the file system path of the working directory to be used when activating the link target. |
| `data.command_line_arguments` | String |  | COMMAND_LINE_ARGUMENTS stores the command-line arguments that are specified when activating the link target. |
| `data.icon_location` | String | FILE_PATH | ICON_LOCATION specifies the location of the icon to be used when displaying a shell link item in an icon view. |
| `extra` | Object |  |  |
| `extra.console_codepage` | Int |  | Unsigned integer that specifies a code page language code identifier. |
| `extra.icon_location` | Object |  | Specifies the path to an icon. The path is encoded using environment variables, which makes it possible to find the icon across machines where the locations vary but are expressed using environment variables. |
| `extra.icon_location.size` | Int |  |  |
| `extra.icon_location.target_ansi` | String |  | Defined by the system default code page, which specifies a path to environment variable information. |
| `extra.icon_location.target_unicode` | String |  | Unicode string that specifies a path to environment variable information. |
| `extra.environmental_variables_location` | Object |  | Specifies a path to environment variable information when the link target refers to a location that has a corresponding environment variable. |
| `extra.environmental_variables_location.size` | Int |  |  |
| `extra.environmental_variables_location.target_ansi` | String |  | Defined by the system default code page, which specifies a path to environment variable information. |
| `extra.environmental_variables_location.target_unicode` | String |  | Unicode string that specifies a path to environment variable information. |
| `extra.darwin_properties` | Object |  | Specifies an application identifier that can be used instead of a link target IDList to install an application when a shell link is activated. |
| `extra.darwin_properties.darwin_data_ansi` | String |  | defined by the system default code page, which specifies an application identifier. This field SHOULD be ignored. |
| `extra.darwin_properties.darwin_data_unicode` | String |  | Unicode string that specifies an application identifier. |
| `extra.darwin_properties.product_code_id` | StringToLower |  | Field created by the parser by interpreting the previous fields? |
| `extra.darwin_properties.feature_name` | String |  | Field created by the parser by interpreting the previous fields? |
| `extra.darwin_properties.component_id` | String |  | Field created by the parser by interpreting the previous fields? |
| `extra.special_folder_location` | Object |  | Specifies the location of a special folder. This data can be used when a link target is a special folder to keep track of the folder, so that the link target IDList can be translated when the link is loaded. |
| `extra.special_folder_location.special_folder_id` | Int |  | Unsigned integer that specifies the folder integer ID. |
| `extra.special_folder_location.special_folder_name` | String |  | Translation of the special_folder_id value. |
| `extra.known_folder_location` | Object |  | Specifies the location of a known folder. This data can be used when a link target is a known folder to keep track of the folder so that the link target IDList can be translated when the link is loaded. |
| `extra.known_folder_location.known_folder_id` | StringToLower |  | GUID packet representation that specifies the folder GUID ID. |
| `extra.metadata_properties` | Object |  | PropertyStoreDataBlock specifies a set of properties that can be used by applications to store extra data in the shell link. |
| `extra.metadata_properties.size` | Int |  |  |
| `extra.metadata_properties.property_store[]` | Array[Object] |  | A serialized property storage structure |
| `extra.metadata_properties.property_store[].version` | String |  | Has to be equal to 0x53505331. |
| `extra.metadata_properties.property_store[].format_id` | String |  | A GUID that specifies the semantics and expected usage of the properties contained in this Serialized Property Storage structure. It MUST be unique in the set of serialized property storage structures. |
| `extra.metadata_properties.property_store[].serialized_property_values[]` | Array[Object] |  |  |
| `extra.metadata_properties.property_store[].serialized_property_values[].value_type` | String |  |  |
| `extra.metadata_properties.property_store[].serialized_property_values[].value` | Dynamic |  |  |
| `extra.metadata_properties.property_store[].serialized_property_values[].id` | Int |  |  |
| `extra.metadata_properties.property_store[].serialized_property_values[].name` | String |  |  |
| `extra.metadata_properties.property_store[].serialized_property_values[].name_size` | Int |  |  |
| `extra.shim_layer_properties` | Object |  | Specifies the name of a shim that can be applied when activating a link target. |
| `extra.shim_layer_properties.name` | String |  | LayerName: unicode string that specifies the name of a shim layer to apply to a link target when it is being activated |
| `extra.distributed_link_tracker` | Object |  | Specifies data that can be used to resolve a link target if it is not found in its original location when the link is resolved. This data is passed to the Link Tracking service to find the link target. |
| `extra.distributed_link_tracker.version` | String |  | This value MUST be 0x00000000. |
| `extra.distributed_link_tracker.machine_identifier` | String |  | Specifies the NetBIOS name of the machine where the link target was last known to reside. |
| `extra.distributed_link_tracker.droid_volume_identifier` | StringToLower | VOLUME_GUID | Two values (a priori droid_volume_identifier and droid_file_identifier) in GUID packet representation that are used to find the link target with the Link Tracking service. |
| `extra.distributed_link_tracker.droid_file_identifier` | StringToLower |  | Two values (a priori droid_volume_identifier and droid_file_identifier) in GUID packet representation that are used to find the link target with the Link Tracking service |
| `extra.distributed_link_tracker.droid_file_mft_seq` | Int |  |  |
| `extra.distributed_link_tracker.droid_file_frn` | IntToHex |  |  |
| `extra.distributed_link_tracker.droid_file_sequence_number` | Int |  |  |
| `extra.distributed_link_tracker.droid_file_record_number` | Int |  |  |
| `extra.distributed_link_tracker.droid_file_mft_seq` | Extension |  |  |
| `extra.distributed_link_tracker.droid_file_frn_hex` | Int |  |  |
| `extra.distributed_link_tracker.droid_file_frn_split` | String |  |  |
| `extra.distributed_link_tracker.droid_file_timestamp` | DateTime |  | Information générée par le parseur grace à la résolution de droid_volume_identifier et droid_file_identifier ? |
| `extra.distributed_link_tracker.droid_file_mac` | String |  | Information générée par le parseur grace à la résolution de droid_volume_identifier et droid_file_identifier ? |
| `extra.distributed_link_tracker.droid_file_vendor` | String |  | Information générée par le parseur grace à la résolution de droid_volume_identifier et droid_file_identifier ? |
| `extra.distributed_link_tracker.birth_droid_volume_identifier` | StringToLower | VOLUME_GUID | Two values (a priori birth_droid_volume_identifier et birth_droid_file_identifier) in GUID packet representation that are used to find the link target with the Link Tracking service. |
| `extra.distributed_link_tracker.birth_droid_file_identifier` | StringToLower |  | Two values (a priori birth_droid_volume_identifier et birth_droid_file_identifier) in GUID packet representation that are used to find the link target with the Link Tracking service. |
| `extra.distributed_link_tracker.birth_droid_file_mft_seq` | Int |  |  |
| `extra.distributed_link_tracker.birth_droid_file_frn` | IntToHex |  |  |
| `extra.distributed_link_tracker.birth_droid_file_sequence_number` | Int |  |  |
| `extra.distributed_link_tracker.birth_droid_file_record_number` | Int |  |  |
| `extra.distributed_link_tracker.birth_droid_file_mft_seq` | Extension |  |  |
| `extra.distributed_link_tracker.birth_droid_file_timestamp` | DateTime |  | Timestamp generated by the parser by resolving birth_droid_volume_identifier and birth_droid_file_identifier? |
| `extra.distributed_link_tracker.birth_droid_file_mac` | String |  | MAC address generated by the parser by resolving birth_droid_volume_identifier and birth_droid_file_identifier? |
| `extra.distributed_link_tracker.birth_droid_file_vendor` | String |  | Vendor information generated by the parser by resolving birth_droid_volume_identifier and birth_droid_file_identifier? |
| `extra.console_properties` | Object |  | Specifies the display settings to use when a link target specifies an application that is run in a console window. |
| `extra.console_properties.size` | Int |  |  |
| `extra.console_properties.fill_attributes` | Int |  | Specifies the fill attributes that control the foreground and background text colors in the console window. |
| `extra.console_properties.popup_fill_attributes` | Int |  | specifies the fill attributes that control the foreground and background text color in the console window popup. The values are the same as for the FillAttributes field. |
| `extra.console_properties.screen_buffer_size_x` | Int |  | Specifies the horizontal size (X axis), in characters, of the console window buffer. |
| `extra.console_properties.screen_buffer_size_y` | Int |  | Specifies the vertical size (Y axis), in characters, of the console window buffer. |
| `extra.console_properties.window_size_x` | Int |  | Specifies the horizontal size (X axis), in characters, of the console window. |
| `extra.console_properties.window_size_y` | Int |  | Specifies the vertical size (Y axis), in characters, of the console window. |
| `extra.console_properties.window_origin_x` | Int |  | Specifies the horizontal coordinate (X axis), in pixels, of the console window origin. |
| `extra.console_properties.window_origin_y` | Int |  | Specifies the vertical coordinate (Y axis), in pixels, of the console window origin. |
| `extra.console_properties.font_size` | Int |  | Specifies the size, in pixels, of the font used in the console window. |
| `extra.console_properties.font_family` | Int |  | Specifies the family of the font used in the console window. This value MUST be comprised of a font family and a font pitch. Voir le tableau de la doc pour interpréter. |
| `extra.console_properties.font_weight` | Int |  | Specifies the stroke weight of the font used in the console window. lower than 700: regular, greater than 700: bold. |
| `extra.console_properties.face_name` | String |  | Specifies the face name of the font used in the console window |
| `extra.console_properties.cursor_size` | Int |  | Specifies the size of the cursor, in pixels, used in the console window. lower than 25: small, 25-50: normal, 51-100: large. |
| `extra.console_properties.full_screen` | Int |  | Specifies whether to open the console window in full-screen mode. 0: windows, other: fullscreen. |
| `extra.console_properties.quick_edit` | Int |  | Specifies whether to open the console window in QuikEdit mode. In QuickEdit mode, the mouse can be used to cut, copy, and paste text in the console window. 0: off, other: on. |
| `extra.console_properties.insert_mode` | Int |  | Specifies insert mode in the console window. 0: disabled, other: enabled. |
| `extra.console_properties.auto_position` | Int |  | Specifies auto-position mode of the console window. 0: false, other: true ; if false, origin x and y are used. |
| `extra.console_properties.history_buffer_size` | Int |  | Specifies the size, in characters, of the buffer that is used to store a history of user input into the console window. |
| `extra.console_properties.number_of_history_buffers` | Int |  | Specifies the number of history buffers to use. |
| `extra.console_properties.history_no_dup` | Int |  | Specifies whether to remove duplicates in the history buffer. 0: duplicates not allowed, other: duplicates allowed |
| `extra.console_properties.color_table` | Int |  | specifying the RGB colors that are used for text in the console window. The values of the fill attribute fields FillAttributes and PopupFillAttributes are used as indexes into this table to specify the final foreground and background color for a character. |
| `extra.shell_item_identifier` | Object |  | The VistaAndAboveIDListDataBlock structure specifies an alternate IDList that can be used instead of the LinkTargetIDList structure on platforms that support it. |
| `extra.shell_item_identifier.id_list[]` | Array[Object] |  | An IDList structure |
| `extra.terminal_properties` | Object |  | A structure that indicates the end of the extra data section. |
| `extra.terminal_properties.size` | Int |  |  |
| `extra.terminal_properties.appended_data_sha256` | String |  |  |
| `extra.terminal_properties.appended_data_base64` | String |  |  |
| `target` | Object |  |  |
| `target.items[]` | Array[Object] |  |  |
| `target.items[].strings[]` | Array[String] |  | Strings extracted from identifiers by the in-house parser |
| `target.items[].identifiers` | Object |  |  |
| `target.items[].item_class` | String |  | Common to every item types (RootFolder, VolumeItem, FileEntry, Internet, ControlPanel, UsersFilesFolder, Unknown). Indicates the type of element (Root Folder, Volume Item, File entry, etc...). |
| `target.items[].sort_index` | String |  | For items type 'RootFolder', should contains the root of the link. |
| `target.items[].guid` | String |  | For items type 'RootFolder', should contains a ShellFolderID. |
| `target.items[].class_type_indicator` | Int |  | Raw form (int) of flags; verify and hide if correct |
| `target.items[].flags` | String |  | For items type 'VolumeItem' and 'FileEntry', contains a flag, possibly as a string if interpreted by the parser (examples: Is directory, Is file) and an int/hex value otherwise. |
| `target.items[].data` | String |  | For items type 'VolumeItem', should contain the volume letter. |
| `target.items[].size` | Int | FILE_SIZE | For items type 'FileEntry', contains the size of the target file (and probably 0 for a directory). |
| `target.items[].modification_time` | DateTime | DATE_MODIFICATION | For items type 'FileEntry', last modification date of the target file? |
| `target.items[].file_attribute_flags` | Int |  | For items type 'FileEntry', target file attributes; interpreted? |
| `target.items[].primary_name` | String |  | For items type 'FileEntry', name of a file or directory in the target path. |
| `target.items[].item_identifier` | String |  | For items type 'ControlPanel' |
| `target.items[].data_base64` | String |  | Base64 content for Unknown item_class values. |
| `target.items[].data_sha256` | String |  | SHA-256 of the content for Unknown item_class values. |
| `target.target_path` | String | FILE_PATH |  |
| `link_info` | Object |  |  |
| `link_info.local_base_path` | String | FILE_PATH |  |
| `link_info.common_path_suffix` | String | FILE_PATH |  |
| `link_info.location` | String |  |  |
| `link_info.location_info` | Object |  |  |
| `link_info.location_info.r_drive_type` | Int |  |  |
| `link_info.location_info.drive_type` | String |  |  |
| `link_info.location_info.drive_serial_number` | String |  |  |
| `link_info.location_info.volume_label` | String |  |  |
| `link_info.location_info.volume_label_unicode` | String |  |  |
| `link_info.location_info.common_network_relative_link_flags` | String |  |  |
| `link_info.location_info.r_network_provider_type` | String |  |  |
| `link_info.location_info.network_provider_type` | String |  |  |
| `link_info.location_info.net_name` | String |  |  |
| `link_info.location_info.net_name_unicode` | String |  |  |
| `link_info.location_info.device_name` | String |  |  |
| `link_info.location_info.device_name_unicode` | String |  |  |
| `slack` | Object |  |  |
| `slack.payload` | String |  |  |
