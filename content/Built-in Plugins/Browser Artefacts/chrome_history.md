---
 title: 'Chrome History'
---


{{< callout type="important" >}}Data Type: **browser_history** \
	Python Parser: **SQLite**{{< /callout >}}

### Description 

Each row represents a Chrome visit, with URL, page title, visit time, visit count, referrer, and hidden state where available. Use it to reconstruct navigation and correlate web activity with downloads, authentication, or endpoint events. Browser history can be incomplete because of deletion, private browsing, retention, or profile selection.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `url`   |
|Additional Description    | `title`   |
|    | `visit_count`   |
|    | `referer`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `url` | String |  | web address that was visited |
| `title` | String |  | title of the visited webpage |
| `visit_date` | DateTime |  | timestamp of the visit |
| `visit_count` | Int |  | total number of times the URL was visited |
| `referer` | String |  | URL of the page that referred to this visit, if available |
| `hidden` | Int |  | flag indicating whether the entry is hidden (1) or not (0) |
