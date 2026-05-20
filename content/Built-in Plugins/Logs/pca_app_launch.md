---
 title: 'Pca App Launch'
---


{{< callout type="important" >}}Data Type: **pca_app_launch** \
	Python Parser: **Regexp**{{< /callout >}}

### Description 

Parses PCA application launch data.

- Captures the exact path of every program launched via PCA.
- Records the precise launch time with sub‑second resolution.
- Stores the data in a simple CSV‑compatible format for easy correlation with other forensic artefacts.
- Helps identify usage of older or compatibility‑mode applications.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `executable_path`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `timestamp` | DateTime |  | timestamp of the application launch |
| `executable_path` | String | FILE_PATH | full path of the executable launched via PCA |
