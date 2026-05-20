---
 title: 'Browser History Lite'
---


{{< callout type="important" >}}Data Type: **browser_history** \
	Python Parser: **SQLite**{{< /callout >}}

### Description 

Extracts navigation records from a Firefox `places` sqlite database. It records each visited
URL together with its title, visit timestamp, visit count, and the referring page (if any).
Each row corresponds to a single page visit, allowing reconstruction of browsing activity over
time.

- URL and page title provide the content accessed.
- Visit timestamp indicates when the page was opened.
- Visit count shows frequency of access.
- Referrer reveals navigation paths.


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
| `url` | String |  | URL of the visited page |
| `title` | String |  | Title of the visited page |
| `visit_date` | DateTime |  | Timestamp when the page was visited |
| `visit_count` | Int |  | Number of times the page has been visited |
| `referer` | String |  | URL of the referring page, if any |
| `hidden` | Int |  | Flag indicating whether the entry is hidden from history (1 = hidden) |
