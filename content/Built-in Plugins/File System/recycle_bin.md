---
 title: 'Recycle Bin'
---


{{< callout type="important" >}}Data Type: **recycle_bin** \
	Python Parser: **RecycleBin**{{< /callout >}}

### Description 

Extracts metadata from Windows recycle‑bin files.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `path`   |
|Additional Description    | `size`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `path` | String | FILE_PATH | original full path of the deleted file before it was sent to the Recycle Bin |
| `size` | Int | FILE_SIZE | size, in bytes, of the original file that was deleted |
| `header` | String |  | INFO2 file version identifier (1 = Vista/7, 2 = Windows 10+) |
| `uninstall_date` | DateTime | DATE_UNINSTALL | timestamp when the file was removed (deleted) and placed in the Recycle Bin |
