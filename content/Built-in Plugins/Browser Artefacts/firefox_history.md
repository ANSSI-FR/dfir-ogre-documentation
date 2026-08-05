---
 title: 'Firefox History'
---


{{< callout type="important" >}}Data Type: **browser_history** \
	Python Parser: **SQLite**{{< /callout >}}

### Description 

Each row represents a Firefox page visit, with URL, title, visit time, visit count, referrer, and hidden state where available. Use it to reconstruct navigation and correlate browsing with downloads, credentials, or endpoint events. History can be incomplete because of deletion, private browsing, retention, synchronization, or profile selection.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Description    | `url`   |
|Additional Description    | `title`   |
|    | `visit_count`   |
|    | `referer`   |

### Fields 

| Output Name | Data Type | Description |
|---|---|---|
| `url` | String | URL of the visited page |
| `title` | String | Title of the visited page |
| `visit_date` | DateTime | Timestamp when the page was visited |
| `visit_count` | Int | Number of times the page has been visited |
| `referer` | String | URL of the referring page, if any |
| `hidden` | Int | Flag indicating whether the entry is hidden from history (1 = hidden) |
