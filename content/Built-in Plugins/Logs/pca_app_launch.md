---
 title: 'Pca App Launch'
---


{{< callout type="important" >}}Data Type: **pca_app_launch** \
	Python Parser: **Regexp**{{< /callout >}}

### Description 

Each row is an application launch recorded by the Windows Program Compatibility Assistant, with executable path and high-resolution launch time. Use it as execution evidence and correlate the path with Prefetch, Amcache, UserAssist, or filesystem records. Coverage and retention vary by Windows version, so absence does not exclude execution.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `executable_path`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `timestamp` | DateTime |  | timestamp of the application launch |
| `executable_path` | String | FILE_PATH | full path of the executable launched via PCA |
