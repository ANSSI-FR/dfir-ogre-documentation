---
 title: 'Browser History'
---


{{< callout type="important" >}}Data Type: **browser_history** \
	Python Parser: **SQLite**{{< /callout >}}

### Description 

Parses the browsing hisory database of a Chrome profile (typically `*/Default/History`). It
extracts each recorded URL, its page title, visit timestamps, the number of times the URL was
visited, and the referer URL if available.

- Shows which web resources a user accessed.
- Provides visit frequency, helping gauge the relevance of each site.
- Captures the referer, offering context about navigation paths.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `url`   |
|Additional Description    | `title`   |
|    | `visit_count`   |
|    | `origin`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `url` | String |  | web address that was visited |
| `title` | String |  | title of the visited webpage |
| `visit_date` | DateTime |  | timestamp of the visit |
| `visit_count` | Int |  | total number of times the URL was visited |
| `referer` | String |  | URL of the page that referred to this visit, if available |
| `hidden` | Int |  | flag indicating whether the entry is hidden (1) or not (0) |
