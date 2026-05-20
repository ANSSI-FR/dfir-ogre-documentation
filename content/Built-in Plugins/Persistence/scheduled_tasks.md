---
 title: 'Scheduled Tasks'
---


{{< callout type="important" >}}Data Type: **scheduled_tasks** \
	Python Parser: **RegScheduledTask**{{< /callout >}}

### Description 

Extracts metadata for Windows scheduled tasks stored in the `Software` hive.

- Retrieves task identifiers, authors, creation/registration dates and version.
- Decodes action blocks (command, arguments, COM data) and links to boot, logon, maintenance and plain sub‑keys.
- Extracts security information, including owner SID and ACLs.


### Timeline 

| Timeline Field | Data Field |
|---|---|
|Related User    | `key_security.owner_sid`   |
|Description    | `task`   |
|Additional Description    | `actions.action_type`   |
|    | `actions.exec_command`   |
|    | `actions.exec_arguments`   |
|    | `actions.com_data`   |

### Fields 

| Output Name | Data Type | Qualifier | Description |
|---|---|---|---|
| `guid` | String | SCHTASK_GUID | unique identifier (GUID) of the scheduled task |
| `uri` | String | SCHTASK_URI | URI associated with the scheduled task |
| `task` | String |  | full registry path of the scheduled task definition |
| `task_description` | String |  | human‑readable description of the task |
| `source` | String |  | origin source of the task |
| `author` | String |  | author or creator of the scheduled task |
| `data` | String |  | raw data blob stored for the task |
| `documentation` | String |  | documentation URL or text linked to the task |
| `hash` | String |  | hex‑encoded hash of the task definition |
| `schema` | Int |  | schema version number of the task definition |
| `trigger` | String |  | trigger configuration that defines when the task runs |
| `version` | String |  | version string of the scheduled task |
| `actions[]` | Array[Object] |  |  |
| `actions[].action_id` | String |  | identifier of the action within the task |
| `actions[].action_type` | String |  | type of action (e.g., Exec, ComHandler, SendEmail, ShowMessage) |
| `actions[].exec_command` | String |  | executable command to run for Exec actions |
| `actions[].exec_arguments` | String |  | command‑line arguments for the executable |
| `actions[].exec_working_dir` | String |  | working directory used when executing the command |
| `actions[].com_classid` | String |  | COM class identifier (CLSID) for ComHandler actions |
| `actions[].com_data` | String |  | additional data passed to the COM handler |
| `actions[].email_from` | String |  | sender address for SendEmail actions |
| `actions[].email_to` | String |  | recipient address(es) for SendEmail actions |
| `actions[].email_cc` | String |  | CC address(es) for SendEmail actions |
| `actions[].email_bcc` | String |  | BCC address(es) for SendEmail actions |
| `actions[].email_replyto` | String |  | Reply‑To address for SendEmail actions |
| `actions[].email_server` | String |  | SMTP server used for SendEmail actions |
| `actions[].email_subject` | String |  | subject line of the email |
| `actions[].email_body` | String |  | body content of the email |
| `actions[].email_attachments` | String |  | list of attachment filenames for the email |
| `actions[].message_body` | String |  | text displayed in the message box for ShowMessage actions |
| `actions[].message_title` | String |  | title of the message box for ShowMessage actions |
| `security_descriptor` | Object |  |  |
| `boot` | Object |  |  |
| `boot.mtime` | DateTime | DATE_MODIFICATION | modification timestamp of the boot sub‑key for the task |
| `logon` | Object |  |  |
| `logon.mtime` | DateTime | DATE_MODIFICATION | modification timestamp of the logon sub‑key for the task |
| `maintenance` | Object |  |  |
| `maintenance.mtime` | DateTime | DATE_MODIFICATION | modification timestamp of the maintenance sub‑key for the task |
| `plain` | Object |  |  |
| `plain.mtime` | DateTime | DATE_MODIFICATION | modification timestamp of the plain sub‑key for the task |
| `tree` | Object |  |  |
| `tree.mtime` | DateTime | DATE_MODIFICATION | modification timestamp of the tree sub‑key for the task |
| `creation_date` | String | DATE_CREATION | timestamp when the scheduled task was initially created |
| `last_run_launch_date` | DateTime | DATE_LAST_RUN | timestamp of the most recent task launch |
| `last_run_exit_code` | Int | EXIT_CODE | exit code returned by the latest execution of the task |
| `last_run_exit_date` | DateTime | DATE_LAST_RUN | timestamp when the latest task execution completed |
| `registration_date_local` | DateTime | DATE_CREATION | date the task was registered |
| `key_path` | String | KEY_PATH | full registry key name |
| `key_modif_time` | DateTime | DATE_MODIFICATION | last modification timestamp of the registry key |
| `key_security` | Object |  |  |
| `key_security.owner_sid` | String | USER_SID | SID of the user that owns the registry key |
| `key_security.group_sid` | String |  | SID of the group that owns the registry key |
| `key_security.control_flags[]` | Array[String] |  | security descriptor control flags for the key |
| `key_security.dacl_ace` | Object |  |  |
| `key_security.dacl_ace.ace_type` | String |  | type of ACE (e.g., allow, deny) |
| `key_security.dacl_ace.account_sid` | String |  | SID of the account the ACE applies to |
| `key_security.dacl_ace.ace_flags[]` | Array[String] |  | ACE flags that modify inheritance or behavior |
| `key_security.dacl_ace.rights[]` | Array[String] |  | permissions granted or denied by the ACE |
