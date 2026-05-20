---
 title: 'Built-in Plugins'
 weight: 3
---

DFIR-OGRE provides a collection of plug‑ins, each dedicated to parsing a specific class of Windows artefacts. The built‑in plug‑ins cover a lot of artefacts that appears in a typical DFIR-ORC archive.

## Retrieving the plugins

Plugins can be retrieved by cloning the `dfir-ogre-plugin-windows` repository

```bash
# Choose a location where you keep all the sources
mkdir -p ~/dfir-ogre && cd ~/dfir-ogre

git clone https://github.com/ANSSI-FR/dfir-ogre-plugin-windows.git
```

The plugins are located in dfir-ogre-plugin-windows/configuration folder

---

## Plugin list

{{< cards >}}
 {{< card link="application-specific/acmru" title="Acmru" subtitle="Extracts Search Assistant  entries from `NTUser` hive" tag="Application Specific" tagColor="green">}}
 {{< card link="services-and-applications/activity_cache" title="Activity Cache" subtitle="Extracts rows from the *Activity* SQLite table that records Windows 10 Timeline events" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="services-and-applications/amcache_driver" title="Amcache Driver" subtitle="Extracts driver metadata stored in the `AmCache` hive" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="services-and-applications/amcache_driver_xml" title="Amcache Driver Xml" subtitle="List drivers from various xml report files" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="services-and-applications/amcache_file" title="Amcache File" subtitle="Retrieves cached executable file metadata from the Windows `AmCache` hive" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="services-and-applications/amcache_ie_addon_xml" title="Amcache Ie Addon Xml" subtitle="List internet explorer addons from different xml report files" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="services-and-applications/amcache_installer_xml" title="Amcache Installer Xml" subtitle="List installed software from various Xml files" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="services-and-applications/amcache_program" title="Amcache Program" subtitle="Extracts metadata about installed programs from the Windows `AmCache` hive" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="services-and-applications/amcache_program_xml" title="Amcache Program Xml" subtitle="Parse installed programs from AEINV WER xml reports" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="services-and-applications/amcache_program_xml_xml" title="Amcache Program Xml XML" subtitle="Parse installed programs from `FullCompatReport` reports" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="services-and-applications/amcache_program_xml_xml" title="Amcache Program Xml XML" subtitle="Parse installed programs from `AEINV_PREVIOUS` reports" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="application-specific/antifishing_file" title="Antifishing File" subtitle="Extracts the Internet Explorer anti‑phishing registry hive under `NTUser` hive" tag="Application Specific" tagColor="green">}}
 {{< card link="services-and-applications/app_compat_cache" title="App Compat Cache" subtitle="Extracts entries from the `AppCompatCache` value stored in the Windows `System` hive" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="persistence/autoruns" title="Autoruns" subtitle="Parses CSV files produced by the Windows Autoruns utility, extracting entries that define programs or scripts that start automatically" tag="Persistence" tagColor="amber">}}
 {{< card link="file-system/backup_exclude" title="Backup Exclude" subtitle="Extracts entries that Windows marks as excluded from Volume Shadow Copy Service (VSS) and backup operations, from the `System` hive" tag="File System" tagColor="green">}}
 {{< card link="services-and-applications/bam_dam" title="Bam Dam" subtitle="Extracts Activity Moderator (BAM/DAM) records from the Windows `System` hive" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="browser-artefacts/browser_download_history" title="Browser Download History" subtitle="Parses the download history database of a Chrome profile (typically `*/Default/History`)" tag="Browser Artefacts" tagColor="red">}}
 {{< card link="browser-artefacts/browser_download_history_lite" title="Browser Download History Lite" subtitle="Extracts records from the `places` sqlite database that Firefox uses to store download metadata" tag="Browser Artefacts" tagColor="red">}}
 {{< card link="browser-artefacts/browser_history" title="Browser History" subtitle="Parses the browsing hisory database of a Chrome profile (typically `*/Default/History`)" tag="Browser Artefacts" tagColor="red">}}
 {{< card link="browser-artefacts/browser_history_lite" title="Browser History Lite" subtitle="Extracts navigation records from a Firefox `places` sqlite database" tag="Browser Artefacts" tagColor="red">}}
 {{< card link="browser-artefacts/chrome_extension" title="Chrome Extension" subtitle="Extracts metadata from a Chrome‑based browser extension’s manifest" tag="Browser Artefacts" tagColor="red">}}
 {{< card link="windows-artefacts/clsid" title="Clsid" subtitle="Enumerates every user‑specific COM class identifier (CLSID) stored in the `UsrClass` hive" tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="windows-artefacts/clsid_software" title="Clsid Software" subtitle="Extracts every CLSID registration stored in the machine‑wide `Software` hive" tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="logs/evt" title="Evt" subtitle="Parse Windows EventLog (EVT) files and emit one record per event" tag="Logs" tagColor="purple">}}
 {{< card link="fast-find/fastfind_file" title="Fastfind File" subtitle="Parse the filesystem results of the fastfind tool" tag="Fast Find" tagColor="indigo">}}
 {{< card link="fast-find/fastfind_obj" title="Fastfind Obj" subtitle="Parse the object result of the fastfind tool" tag="Fast Find" tagColor="indigo">}}
 {{< card link="fast-find/fastfind_reg" title="Fastfind Reg" subtitle="Parse the registry results of the fastfind tool" tag="Fast Find" tagColor="indigo">}}
 {{< card link="browser-artefacts/firefox_extension" title="Firefox Extension" subtitle="Extracts metadata from Firefox browser add‑ons (version 26+)" tag="Browser Artefacts" tagColor="red">}}
 {{< card link="file-system/getthis" title="Getthis" subtitle="Parse the `GetThis` files produced by Orc and retrieve information about the       collected files" tag="File System" tagColor="green">}}
 {{< card link="browser-artefacts/ie_webcache_history" title="Ie Webcache History" subtitle="Extracts browsing history records from Internet Explorer 10+ WebCache databases (WebCacheV01" tag="Browser Artefacts" tagColor="red">}}
 {{< card link="application-specific/java_idx" title="Java Idx" subtitle="Extracts metadata about each downloaded artifact, including its URL, server IP, size, timestamps and signing status" tag="Application Specific" tagColor="green">}}
 {{< card link="services-and-applications/listdlls" title="Listdlls" subtitle="Parse output from Sysinternals **ListDLL** tool that lists loaded DLLs for running processes on Windows" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="windows-artefacts/lnk" title="Lnk" subtitle="Extracts every pieces of metadata that is stored in a Windows Shell Link file" tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="file-system/mass_storage" title="Mass Storage" subtitle="Extracts information about every USB (or other) mass‑storage device ever connected to a Windows system, using data from the `System` hive" tag="File System" tagColor="green">}}
 {{< card link="file-system/merge_file" title="Merge File" subtitle="Reads a text file and concatenates every line into a single output line" tag="File System" tagColor="green">}}
 {{< card link="services-and-applications/mui_cache" title="Mui Cache" subtitle="Extracts entries from the per‑user MUI cache stored in the `Registry` hive" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="system-information/network_config" title="Network Config" subtitle="Extracts network settings from the Windows `System` hive" tag="System Information" tagColor="indigo">}}
 {{< card link="file-system/ntfsinfo" title="Ntfsinfo" subtitle="Extract NTFS's Master File Table (MFT) from an ORC‑generated CSV file" tag="File System" tagColor="green">}}
 {{< card link="windows-artefacts/objinfo" title="Objinfo" subtitle="Parses files produced by the GetObjInfo utility, extracting Windows object information from the object manager namespace" tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="logs/pca_app_launch" title="Pca App Launch" subtitle="Parses PCA application launch data" tag="Logs" tagColor="purple">}}
 {{< card link="logs/pca_general_record" title="Pca General Record" subtitle="Extracts each line of a PCA log" tag="Logs" tagColor="purple">}}
 {{< card link="file-system/pending_rename" title="Pending Rename" subtitle="Extracts entries from the `PendingFileRenameOperations` value in the `System` hive" tag="File System" tagColor="green">}}
 {{< card link="services-and-applications/prefetch" title="Prefetch" subtitle="Parses Windows Prefetch files to extract execution metadata" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="services-and-applications/processes_orc" title="Processes Orc" subtitle="Extracts Windows processes data from an ORC‑generated CSV file" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="services-and-applications/processes_orc_csv" title="Processes Orc Csv" subtitle="Parses CSV files produced by ORC that enumerate running processes" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="services-and-applications/recent_app" title="Recent App" subtitle="Extracts information about applications and files recently accessed by a user from the `NtUser` hive" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="file-system/recycle_bin" title="Recycle Bin" subtitle="Extracts metadata from Windows recycle‑bin files" tag="File System" tagColor="green">}}
 {{< card link="persistence/reg_autoruns" title="Reg Autoruns" subtitle="Extracts persistence‑related registry data from the USER hive (HKCU)" tag="Persistence" tagColor="amber">}}
 {{< card link="persistence/reg_autoruns_software" title="Reg Autoruns Software" subtitle="Extracts persistence‑related registry data from the SOFTWARE hive" tag="Persistence" tagColor="amber">}}
 {{< card link="persistence/reg_autoruns_system" title="Reg Autoruns System" subtitle="Extracts persistence‑related registry data from the SYSTEM hive" tag="Persistence" tagColor="amber">}}
 {{< card link="windows-artefacts/reg_keys" title="Reg Keys" subtitle="Extracts detailed information from Windows Registry hive files" tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="system-information/reg_systeminfo" title="Reg Systeminfo" subtitle="Extracts various system information from the SYSTEM and SOFTWARE hives" tag="System Information" tagColor="indigo">}}
 {{< card link="services-and-applications/run_mru" title="Run Mru" subtitle="Extracts entries from the `RunMRU` in the `NTUser` hive, which stores commands typed in the `Windows + R` dialog" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="persistence/scheduled_tasks" title="Scheduled Tasks" subtitle="Extracts metadata for Windows scheduled tasks stored in the `Software` hive" tag="Persistence" tagColor="amber">}}
 {{< card link="persistence/services_control_set" title="Services Control Set" subtitle="Extracts all service definitions from a Windows `System` hive, in the related control‑set keys" tag="Persistence" tagColor="amber">}}
 {{< card link="file-system/shellbags" title="Shellbags" subtitle="Extracts the contents of Shell Bag structures stored in the `UsrClass` hive" tag="File System" tagColor="green">}}
 {{< card link="services-and-applications/shim_db" title="Shim Db" subtitle="Extracts information about the Windows Application Compatibility Shim database stored in the `Software` hive" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="services-and-applications/srum_app_timeline" title="Srum App Timeline" subtitle="Srum table that tracks statistics about inputs (focus, keyboard, mouse, etc" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="services-and-applications/srum_application_resources" title="Srum Application Resources" subtitle="Srum table that tracks ressource usage for every exe that’s executed on the system       whether it still exists on disk or not" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="services-and-applications/srum_energy_estimation" title="Srum Energy Estimation" subtitle="Parse data from srum" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="windows-artefacts/srum_energy_usage" title="Srum Energy Usage" subtitle="Srum table that tracks stores the per‑process estimates of how much electrical       energy Windows thinks each component has consumed over time" tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="windows-artefacts/srum_energy_usage_long_term" title="Srum Energy Usage Long Term" subtitle="Srum table that tracks long term, per‑process estimates of how much electrical       energy Windows thinks each component has consumed over time" tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="network/srum_network_connectivity_usage" title="Srum Network Connectivity Usage" subtitle="Srum table that tracks network connection time statistics per interface" tag="Network" tagColor="indigo">}}
 {{< card link="network/srum_network_data_usage" title="Srum Network Data Usage" subtitle="SRUM table that tracks how much network traffic each installed app consumes" tag="Network" tagColor="indigo">}}
 {{< card link="services-and-applications/srum_sdp_cpu" title="Srum Sdp Cpu" subtitle="Srum table for windows server 2022 that tracks cpu time" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="network/srum_sdp_network" title="Srum Sdp Network" subtitle="Srum table for windows server 2022 that tracks network activity" tag="Network" tagColor="indigo">}}
 {{< card link="file-system/srum_sdp_physical_disk" title="Srum Sdp Physical Disk" subtitle="Srum table for windows server 2022 that tracks physical drive information" tag="File System" tagColor="green">}}
 {{< card link="file-system/srum_sdp_volume" title="Srum Sdp Volume" subtitle="Srum table for windows server 2022 that tracks storage volumes information" tag="File System" tagColor="green">}}
 {{< card link="windows-artefacts/srum_tagged_energy" title="Srum Tagged Energy" subtitle="Parse data from Srum `tagged_energy` table       ```{B6D82AF1-F780-4E17-8077-6CB9AD8A6FC4}```       ()" tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="windows-artefacts/srum_vfuprov" title="Srum Vfuprov" subtitle="Parse data from Srum `vfuprov` table ```{7ACBBAA3-D029-4BE4-9A7A-0885927F1D8F}```" tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="windows-artefacts/srum_wpn_provider" title="Srum Wpn Provider" subtitle="Srum table that tracks telemetry that Windows collects about the Windows Push       Notification (WPN) service – i" tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="services-and-applications/subject_interface_package" title="Subject Interface Package" subtitle="Extracts Subject Interface Package (SIP) records from the Windows `Software` hive" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="system-information/systeminfo" title="Systeminfo" subtitle="Parses the Windows SystemInfo CSV file generated by the `systeminfo` command" tag="System Information" tagColor="indigo">}}
 {{< card link="network/tcpvcon" title="Tcpvcon" subtitle="Parse a TCPView “Tcpvcon" tag="Network" tagColor="indigo">}}
 {{< card link="services-and-applications/user_assist" title="User Assist" subtitle="Extracts execution data stored in the `NTUser` hive" tag="Services and Applications" tagColor="indigo">}}
 {{< card link="system-information/user_profile" title="User Profile" subtitle="Extracts data about Windows user profiles from the `Software` hive" tag="System Information" tagColor="indigo">}}
 {{< card link="file-system/usninfo" title="Usninfo" subtitle="Parses the CSV export of the Windows USN Journal" tag="File System" tagColor="green">}}
 {{< card link="file-system/volstats" title="Volstats" subtitle="Parses a Windows volume‑statistics csv file" tag="File System" tagColor="green">}}
 {{< card link="file-system/vss_snapshot" title="Vss Snapshot" subtitle="Parses CSV files that list Volume Shadow Copy (VSS) snapshots" tag="File System" tagColor="green">}}
 {{< card link="logs/wer" title="Wer" subtitle="ParsesWindows Error Reporting files (WER), extracting metadata about crashes,       hangs, and other failure events reported by the operating system" tag="Logs" tagColor="purple">}}
 {{< card link="logs/windows_events" title="Windows Events" subtitle="Parses windows evtx logs" tag="Logs" tagColor="purple">}}
 {{< card link="system-information/x509_cert" title="X509 Cert" subtitle="Parses the Windows `Software` registry hive to collect system‑wide X509 certificates stored in the `Software` hive" tag="System Information" tagColor="indigo">}}
 {{< card link="system-information/x509_cert_certificates" title="X509 Cert Certificates" subtitle="Extracts X509 certificates stored in a user’s `NTUser` hive" tag="System Information" tagColor="indigo">}}
{{< /cards >}}
