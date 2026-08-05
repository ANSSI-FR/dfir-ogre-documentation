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
 {{< card link="application-specific/acmru" title="Acmru" subtitle="Shows Windows XP Search Assistant queries with category, recency order, user ownership, and registry timestamps." tag="Application Specific" tagColor="green">}}
 {{< card link="services-and-applications/activity_cache" title="Activity Cache" subtitle="Shows Windows Activities Cache application activity, operation times, status, payloads, and provenance." tag="Services and Applications" tagColor="blue">}}
 {{< card link="services-and-applications/amcache_driver" title="Amcache Driver" subtitle="Shows Amcache driver names, paths, hashes, versions, vendors, sizes, compilation times, and registry metadata." tag="Services and Applications" tagColor="blue">}}
 {{< card link="services-and-applications/amcache_driver_xml" title="Amcache Driver Xml" subtitle="Lists driver hashes, names, versions, vendors, sizes, and compilation metadata from Amcache XML reports." tag="Services and Applications" tagColor="blue">}}
 {{< card link="services-and-applications/amcache_files" title="Amcache Files" subtitle="Shows Amcache executable file paths, hashes, sizes, versions, vendors, timestamps, programs, and registry metadata." tag="Services and Applications" tagColor="blue">}}
 {{< card link="services-and-applications/amcache_ie_addon_xml" title="Amcache Ie Addon Xml" subtitle="Lists Internet Explorer add-on identifiers, names, types, and publishers from Amcache XML reports." tag="Services and Applications" tagColor="blue">}}
 {{< card link="services-and-applications/amcache_installer_xml" title="Amcache Installer Xml" subtitle="Lists installed software, installation times, hashes, versions, vendors, and file metadata from Amcache XML reports." tag="Services and Applications" tagColor="blue">}}
 {{< card link="services-and-applications/amcache_program" title="Amcache Program" subtitle="Shows Amcache installed programs with names, versions, publishers, install dates, paths, and MSI identifiers." tag="Services and Applications" tagColor="blue">}}
 {{< card link="services-and-applications/amcache_program_previous" title="Amcache Program Previous" subtitle="Lists installed programs and executable hashes, paths, versions, vendors, and run evidence from AEINV_PREVIOUS." tag="Services and Applications" tagColor="blue">}}
 {{< card link="services-and-applications/amcache_program_report" title="Amcache Program Report" subtitle="Lists installed programs and executable hashes, paths, versions, vendors, and run evidence from FullCompatReport." tag="Services and Applications" tagColor="blue">}}
 {{< card link="services-and-applications/amcache_program_wer" title="Amcache Program Wer" subtitle="Lists installed programs and executable hashes, paths, versions, vendors, and run evidence from AEINV WER reports." tag="Services and Applications" tagColor="blue">}}
 {{< card link="application-specific/antifishing_file" title="Antifishing File" subtitle="Shows the Internet Explorer anti-phishing user file with registry path, timestamp, owner, and access controls." tag="Application Specific" tagColor="green">}}
 {{< card link="services-and-applications/app_compat_cache" title="App Compat Cache" subtitle="Shows AppCompatCache executable paths, file modification times, cache flags, and registry metadata." tag="Services and Applications" tagColor="blue">}}
 {{< card link="persistence/autoruns" title="Autoruns" subtitle="Shows autorun entries, launch commands, registry locations, users, signatures, hashes, and enabled state." tag="Persistence" tagColor="red">}}
 {{< card link="persistence/autoruns_reg_software" title="Autoruns Reg Software" subtitle="Shows machine-wide SOFTWARE-hive autorun locations, persistence types, values, timestamps, owners, and permissions." tag="Persistence" tagColor="red">}}
 {{< card link="persistence/autoruns_reg_system" title="Autoruns Reg System" subtitle="Shows SYSTEM-hive autorun locations, persistence types, values, timestamps, owners, and permissions." tag="Persistence" tagColor="red">}}
 {{< card link="persistence/autoruns_reg_user" title="Autoruns Reg User" subtitle="Shows per-user autorun locations, persistence types, values, timestamps, owners, and permissions." tag="Persistence" tagColor="red">}}
 {{< card link="file-system/backup_exclude" title="Backup Exclude" subtitle="Shows files and folders excluded from VSS or backups with exclusion type, path, owner, and registry timestamp." tag="File System" tagColor="yellow">}}
 {{< card link="services-and-applications/bam_dam" title="Bam Dam" subtitle="Shows BAM and DAM executable execution evidence with user SIDs, run times, paths, and registry metadata." tag="Services and Applications" tagColor="blue">}}
 {{< card link="windows-artefacts/clsid_software" title="CLSID Software" subtitle="Shows machine-wide COM registrations with CLSIDs, descriptions, executables, redirects, and registry metadata." tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="windows-artefacts/clsid_users" title="CLSID Users" subtitle="Shows per-user COM registrations with CLSIDs, descriptions, executables, redirects, and registry metadata." tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="browser-artefacts/chrome_download_history" title="Chrome Download History" subtitle="Shows Chrome downloads with source URLs, saved paths, timestamps, sizes, states, and danger indicators." tag="Browser Artefacts" tagColor="red">}}
 {{< card link="browser-artefacts/chrome_extension" title="Chrome Extension" subtitle="Shows Chrome extension identity, version, source, permissions, scripts, resources, and security policy." tag="Browser Artefacts" tagColor="red">}}
 {{< card link="browser-artefacts/chrome_history" title="Chrome History" subtitle="Shows Chrome URL visits with titles, timestamps, visit counts, referrers, and hidden status." tag="Browser Artefacts" tagColor="red">}}
 {{< card link="logs/evt" title="Evt" subtitle="Shows legacy Windows EVT events with provider, ID, message data, user, host, timestamps, and recovery status." tag="Logs" tagColor="purple">}}
 {{< card link="application-specific/explorer_search_history" title="Explorer Search History" subtitle="Shows Explorer search queries in recency order with value indexes, user ownership, and registry timestamps." tag="Application Specific" tagColor="green">}}
 {{< card link="fast-find/fastfind_file" title="Fastfind File" subtitle="Shows FastFind filesystem matches with paths, NTFS identifiers, timestamps, attributes, hashes, and match context." tag="Fast Find" tagColor="yellow">}}
 {{< card link="fast-find/fastfind_object" title="Fastfind Object" subtitle="Shows FastFind Windows object matches with object type, name, path, and match description." tag="Fast Find" tagColor="yellow">}}
 {{< card link="fast-find/fastfind_registry" title="Fastfind Registry" subtitle="Shows FastFind registry matches with hive and key paths, values, data, timestamps, and snapshot context." tag="Fast Find" tagColor="yellow">}}
 {{< card link="browser-artefacts/firefox_download_history" title="Firefox Download History" subtitle="Shows Firefox downloads with source URLs, saved paths, timestamps, sizes, and deletion state." tag="Browser Artefacts" tagColor="red">}}
 {{< card link="browser-artefacts/firefox_extension" title="Firefox Extension" subtitle="Shows Firefox add-on identity, version, source, permissions, origins, and installation or update times." tag="Browser Artefacts" tagColor="red">}}
 {{< card link="browser-artefacts/firefox_history" title="Firefox History" subtitle="Shows Firefox URL visits with titles, timestamps, visit counts, referrers, and hidden status." tag="Browser Artefacts" tagColor="red">}}
 {{< card link="file-system/getthis" title="Getthis" subtitle="Shows files collected by ORC GetThis with paths, NTFS identifiers, sizes, hashes, timestamps, and match reasons." tag="File System" tagColor="yellow">}}
 {{< card link="windows-artefacts/hive" title="Hive" subtitle="Shows raw Windows Registry keys and values with modification times, data types, owners, and access controls." tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="file-system/i30_info" title="I30 info" subtitle="Shows NTFS directory-index entries with paths, record identifiers, timestamps, sizes, attributes, and carving status." tag="File System" tagColor="yellow">}}
 {{< card link="browser-artefacts/ie_webcache_history" title="Ie Webcache History" subtitle="Shows Internet Explorer WebCache visits with URLs, cached files, timestamps, access counts, headers, and redirects." tag="Browser Artefacts" tagColor="red">}}
 {{< card link="application-specific/java_idx" title="Java Idx" subtitle="Shows Java cache downloads with URLs, server IPs, sizes, timestamps, completion state, and signing status." tag="Application Specific" tagColor="green">}}
 {{< card link="services-and-applications/list_dlls" title="List Dlls" subtitle="Shows DLLs loaded by running processes with process IDs, command lines, module paths, base addresses, and sizes." tag="Services and Applications" tagColor="blue">}}
 {{< card link="windows-artefacts/lnk" title="Lnk" subtitle="Shows Windows shortcut and Jump List targets, arguments, timestamps, volume data, link flags, and extra metadata." tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="file-system/mass_storage" title="Mass Storage" subtitle="Shows connected mass-storage devices with USB identifiers, serials, volume names, drive letters, users, and timestamps." tag="File System" tagColor="yellow">}}
 {{< card link="file-system/merge_file" title="Merge File" subtitle="Provides the complete text of a multiline artefact as one normalized record for downstream analysis." tag="File System" tagColor="yellow">}}
 {{< card link="services-and-applications/mui_cache" title="Mui Cache" subtitle="Shows per-user MUI cache executable paths and display descriptions with registry ownership and timestamps." tag="Services and Applications" tagColor="blue">}}
 {{< card link="system-information/network_configuration" title="Network Configuration" subtitle="Shows Windows IP, mask, gateway, DHCP, DNS, interface, registry ownership, and configuration timestamps." tag="System Information" tagColor="indigo">}}
 {{< card link="file-system/ntfs_info" title="Ntfs Info" subtitle="Shows MFT file records with paths, NTFS identifiers, timestamps, attributes, hashes, and executable metadata." tag="File System" tagColor="yellow">}}
 {{< card link="windows-artefacts/object_info" title="Object Info" subtitle="Shows Windows object-manager entries with types, namespace paths, symbolic-link targets, and creation times." tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="logs/pca_app_launch" title="Pca App Launch" subtitle="Shows Program Compatibility Assistant application launches with executable paths and precise timestamps." tag="Logs" tagColor="purple">}}
 {{< card link="logs/pca_general_record" title="Pca General Record" subtitle="Shows Program Compatibility Assistant execution records with paths, times, status, vendor, version, and exit code." tag="Logs" tagColor="purple">}}
 {{< card link="file-system/pending_rename" title="Pending Rename" subtitle="Shows file rename or deletion operations queued for reboot with source and target paths plus registry metadata." tag="File System" tagColor="yellow">}}
 {{< card link="services-and-applications/prefetch" title="Prefetch" subtitle="Shows Windows Prefetch execution evidence with executable names, run counts, last-run times, loaded files, and volumes." tag="Services and Applications" tagColor="blue">}}
 {{< card link="services-and-applications/processes_orc_v1" title="Processes Orc V1" subtitle="Shows ORC process records with names, paths, command lines, IDs, parent IDs, sessions, and timestamps." tag="Services and Applications" tagColor="blue">}}
 {{< card link="services-and-applications/processes_orc_v2" title="Processes Orc V2" subtitle="Shows ORC process records with identity, ancestry, command lines, users, timestamps, resource use, and status." tag="Services and Applications" tagColor="blue">}}
 {{< card link="services-and-applications/recent_app" title="Recent App" subtitle="Shows Windows RecentApps launch counts and access times plus recently used file paths and arguments." tag="Services and Applications" tagColor="blue">}}
 {{< card link="file-system/recycle_bin" title="Recycle Bin" subtitle="Shows Recycle Bin entries with original paths, deletion times, sizes, and format headers." tag="File System" tagColor="yellow">}}
 {{< card link="services-and-applications/run_mru" title="Run Mru" subtitle="Shows commands entered in the Windows Run dialog with MRU order, user ownership, and registry timestamps." tag="Services and Applications" tagColor="blue">}}
 {{< card link="persistence/scheduled_tasks" title="Scheduled Tasks" subtitle="Shows scheduled-task identity, triggers, actions, commands, arguments, authorship, timing, and registry security." tag="Persistence" tagColor="red">}}
 {{< card link="persistence/services_control_set" title="Services Control Set" subtitle="Shows Windows service names, start modes, executable paths, accounts, dependencies, parameters, and registry metadata." tag="Persistence" tagColor="red">}}
 {{< card link="file-system/shellbags" title="Shellbags" subtitle="Shows folders browsed in Explorer with reconstructed paths, item metadata, timestamps, users, and registry provenance." tag="File System" tagColor="yellow">}}
 {{< card link="services-and-applications/shim_database" title="Shim Database" subtitle="Shows installed application-compatibility shim databases with GUIDs, target paths, install times, and registry metadata." tag="Services and Applications" tagColor="blue">}}
 {{< card link="services-and-applications/srum_app_timeline" title="Srum App Timeline" subtitle="Shows per-application focus, input, audio, network, and duration statistics recorded by Windows SRUM." tag="Services and Applications" tagColor="blue">}}
 {{< card link="services-and-applications/srum_application_resources" title="Srum Application Resources" subtitle="Shows per-application CPU, I/O, foreground, and background resource usage over time from Windows SRUM." tag="Services and Applications" tagColor="blue">}}
 {{< card link="services-and-applications/srum_energy_estimation" title="Srum Energy Estimation" subtitle="Preserves opaque per-application SRUM energy-estimation records with application, user, and timestamp context." tag="Services and Applications" tagColor="blue">}}
 {{< card link="windows-artefacts/srum_energy_usage" title="Srum Energy Usage" subtitle="Shows SRUM battery energy events with state transitions, capacity, charge level, cycle count, and timestamps." tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="windows-artefacts/srum_energy_usage_long_term" title="Srum Energy Usage Long Term" subtitle="Shows long-term SRUM energy estimates by application, user, power source, activity state, and capacity." tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="network/srum_network_connectivity_usage" title="Srum Network Connectivity Usage" subtitle="Shows SRUM network connection sessions with application, user, interface, profile, start time, and duration." tag="Network" tagColor="yellow">}}
 {{< card link="network/srum_network_data_usage" title="Srum Network Data Usage" subtitle="Shows per-application SRUM network traffic with users, interfaces, profiles, timestamps, and byte counts." tag="Network" tagColor="yellow">}}
 {{< card link="services-and-applications/srum_sdp_cpu" title="Srum Sdp Cpu" subtitle="Shows Windows Server SRUM processor time with application, user, and timestamp context." tag="Services and Applications" tagColor="blue">}}
 {{< card link="network/srum_sdp_network" title="Srum Sdp Network" subtitle="Shows Windows Server SRUM inbound, outbound, and total network bytes by application, user, and time." tag="Network" tagColor="yellow">}}
 {{< card link="file-system/srum_sdp_physical_disk" title="Srum Sdp Physical Disk" subtitle="Shows Windows Server SRUM physical-disk sizes with application, user, and timestamp context." tag="File System" tagColor="yellow">}}
 {{< card link="file-system/srum_sdp_volume" title="Srum Sdp Volume" subtitle="Shows Windows Server SRUM storage-volume capacity and usage with application, user, and timestamp context." tag="File System" tagColor="yellow">}}
 {{< card link="windows-artefacts/srum_tagged_energy" title="Srum Tagged Energy" subtitle="Shows SRUM tagged-energy records with application, user, and timestamp identifiers for correlation." tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="windows-artefacts/srum_vfuprov" title="Srum Vfuprov" subtitle="Shows SRUM VFU provider records with application, user, and timestamp identifiers for correlation." tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="windows-artefacts/srum_wpn_provider" title="Srum Wpn Provider" subtitle="Shows SRUM push-notification activity with application, user, notification type, payload size, and network type." tag="Windows Artefacts" tagColor="amber">}}
 {{< card link="services-and-applications/subject_interface_package" title="Subject Interface Package" subtitle="Shows Subject Interface Packages with GUIDs, names, DLL paths, entry points, owners, and registry timestamps." tag="Services and Applications" tagColor="blue">}}
 {{< card link="system-information/system_info_reg" title="System Info Reg" subtitle="Shows Windows host identity, OS version, build, install and shutdown times, role, architecture, and timezone." tag="System Information" tagColor="indigo">}}
 {{< card link="system-information/systeminfo" title="Systeminfo" subtitle="Shows Windows host, OS, installation, boot, hardware, BIOS, processor, network, and update information." tag="System Information" tagColor="indigo">}}
 {{< card link="network/tcp_connections" title="Tcp Connections" subtitle="Shows captured Windows TCP and UDP endpoints with owning processes, connection state, and local or remote addresses." tag="Network" tagColor="yellow">}}
 {{< card link="services-and-applications/user_assist" title="User Assist" subtitle="Shows per-user program execution counts, focus metrics, launch types, last-run times, and registry provenance." tag="Services and Applications" tagColor="blue">}}
 {{< card link="system-information/user_profile" title="User Profile" subtitle="Shows Windows user profiles with SIDs, paths, hidden or admin status, state, timestamps, and registry permissions." tag="System Information" tagColor="indigo">}}
 {{< card link="file-system/usn_info" title="Usn Info" subtitle="Shows USN Journal file changes with paths, NTFS identifiers, timestamps, reasons, attributes, and source snapshots." tag="File System" tagColor="yellow">}}
 {{< card link="file-system/volstats" title="Volstats" subtitle="Shows Windows volumes with identifiers, mount points, types, locations, shadow-copy IDs, and collected artefact sets." tag="File System" tagColor="yellow">}}
 {{< card link="file-system/vss_snapshot" title="Vss Snapshot" subtitle="Shows Volume Shadow Copy snapshots with snapshot IDs, source volumes, device paths, creation times, and attributes." tag="File System" tagColor="yellow">}}
 {{< card link="logs/wer_reports" title="Wer Reports" subtitle="Shows Windows Error Reporting events with application, crash or hang metadata, timestamps, status, and report IDs." tag="Logs" tagColor="purple">}}
 {{< card link="logs/windows_events" title="Windows Events" subtitle="Shows Windows EVTX events with timestamps, providers, event IDs, users, hosts, processes, and event data." tag="Logs" tagColor="purple">}}
 {{< card link="system-information/x509_certificates_users" title="X509 Certificates Users" subtitle="Shows per-user X.509 certificates with subjects, issuers, validity, keys, fingerprints, and registry provenance." tag="System Information" tagColor="indigo">}}
 {{< card link="system-information/x509cert_software" title="X509Cert Software" subtitle="Shows machine-wide X.509 certificates with subjects, issuers, validity, keys, fingerprints, and registry provenance." tag="System Information" tagColor="indigo">}}
{{< /cards >}}
