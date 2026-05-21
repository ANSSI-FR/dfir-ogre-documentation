---
date: '2026-01-06T15:49:13+01:00'
cascade:
  type: docs
  params:
    breadcrumbs: false
title: 'DFIR-OGRE'
---

**DFIR-OGRE** is a command‑line utility that extract windows forensic artefacts from [DFIR-ORC](https://github.com/DFIR-ORC/dfir-orc) archives into structured data that can be consumed by Splunk, ELK or other databases.

It provides a collection of **plug‑ins**, each dedicated to parsing a specific class of Windows artefacts. The built‑in plug‑ins cover a lot of artefacts that appears in a typical DFIR-ORC archive:

* **Browser artefacts** – Chrome and Firefox extensions, download histories, and general browsing history.  
* **File system** – NTFS information, USN journal entries, Lnk, recycle‑bin, etc. 
* **Persistence mecanism** – Autoruns, Services, Scheduled tasks, etc.
* **Services and applications** – Activity Cache, AmCache, Shell Bags, Prefetch Files, etc.
* **System logs** – Windows Event logs (EVTX), Windows Error Reporting files, SRUM usage databases, etc.

{{< cards cols="2">}}
  {{< card link="getting-started" title="Getting Started" subtitle="Learn how to install DFIR-Ogre " >}}
  {{< card link="usage" title="Usage" subtitle="Learn how to use DFIR-OGRE" >}}
  {{< card link="built-in-plugins" title="Built-in Plugins" subtitle="Explore the list of available plugins" >}}
  {{< card link="plugin-creation" title="Plugin Creation" subtitle="learn how to create custom plugins" >}}
{{< /cards >}}
