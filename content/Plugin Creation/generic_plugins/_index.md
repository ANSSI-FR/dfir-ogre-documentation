---
date: '2026-01-06T15:54:09+01:00'
title: 'Creating Generic Plugins'
cascade:
  type: docs
  params:
    breadcrumbs: true
weight: 2
---
DFIR-OGRE provide generic parser that allows you to parse artefacts by simply defining a XML descriptor file, without the need to create python code.
The following data types are supported
 - [CSV](/plugin-creation/generic_plugins/csv_tutorial/), 
 - [Regular Expression](/plugin-creation/generic_plugins/regexp_plugin/) (extracts artefacts from text files using a regular expression), 
 - [Sqlite](/plugin-creation/generic_plugins/sqlite_plugin/) 
 - [XML](/plugin-creation/generic_plugins/xml_plugin/) ,

The [CSV tutorial](/plugin-creation/generic_plugins/csv_tutorial/) provides a detailled step by step tutorial on how to create and use the descriptor.
The others only describes the specificity of each parsers and how to use them.
