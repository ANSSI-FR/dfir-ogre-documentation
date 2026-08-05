---
 title: 'Recycle Bin'
---


{{< callout type="important" >}}Data Type: **recycle_bin** \
	Python Parser: **RecycleBin**{{< /callout >}}

### Description 

Each row represents Recycle Bin metadata for a deleted item, with original path, item size, deletion time, and format header. Use it to place a file or directory in a deletion timeline and correlate its former location with filesystem records. It does not identify the actor or prove permanent deletion, and metadata may be absent after cleanup or bypassing the Recycle Bin.


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
