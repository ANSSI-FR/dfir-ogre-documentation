---
date: '2026-01-06T15:55:36+01:00'
title: 'XML Descriptor documentation'
weight: 4
---
## Overview

The DFIR-OGRE plugin configuration is an XML file that defines how a parser plugin should read, transform, and structure data from various file formats (CSV, JSON, EVTX, Hive, SQLite, logs, etc.). It maps raw input fields to typed output fields, applies transformations, and optionally defines timeline display behavior.

---

## Quick Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<plugin parser="Csv" file_encoding="UTF-8">
  <mapping data_type="ntfs_info">
    <description>Parse data from the NTFS Info csv file</description>
    <default_parser value="Ignore" />
    <default_date_pattern value="iso" />
    <csv_delimiter value="," />

    <timeline>
      <timeline_type value="Normal" />
      <description>
        <output_name value="snapshot_id" />
      </description>
      <additional_description>
        <output_name value="file_size" />
      </additional_description>
    </timeline>

    <fields>
      <field input="SnapshotID" output="snapshot_id" parser="String" />
      <field input="FileNameCreationDate" output="fn_creation_date" parser="DateTime" />
      <field input="SizeInBytes" output="file_size" parser="Int"/>
    </fields>
  </mapping>
</plugin>
```

---

## 1. Root Element: `<plugin>`

The root element must be named `plugin` and carries two attributes:

| Attribute         | Required | Default  | Description                                              |
| ----------------- | -------- | -------- | -------------------------------------------------------- |
| `parser`          | **Yes**  | -        | Name of the parser associated with this plugin (e.g., `"Csv"`, `"Json"`, `"Evtx"`) |
| `file_encoding`   | No       | `"UTF_8"` | Character encoding for reading the source data files     |

```xml
<plugin parser="Csv" file_encoding="UTF_8">
  ...
</plugin>
```
the following Charaters encoding are supported:
- "`UTF_8`" 
- "`UTF_16_BE`" 
- "`UTF_16_LE`" 
- "`WINDOWS_1250`" 
- "`WINDOWS_1251`" 
- "`WINDOWS_1252`" 
- "`WINDOWS_1253`" 
- "`WINDOWS_1254`" 
- "`WINDOWS_1255`" 
- "`WINDOWS_1256`" 
- "`WINDOWS_1257`"
- "`WINDOWS_1258`"
- "`ISO_2022_JP`"
- "`ISO_8859_2`"
- "`ISO_8859_3`"
- "`ISO_8859_4`"
- "`ISO_8859_5`"
- "`ISO_8859_6`"
- "`ISO_8859_7`"
- "`ISO_8859_8`"
- "`ISO_8859_10`"
- "`ISO_8859_13`"
- "`ISO_8859_14`"
- "`ISO_8859_15`"
- "`IBM866`"

---

## 2. `<mapping>` Element

One or more `<mapping>` elements define how a specific data type is parsed.

| Attribute      | Required | Description                                         |
| -------------- | -------- | --------------------------------------------------- |
| `data_type`    | **Yes**  | Name of the data type this mapping describes          |

Inside `<mapping>`, the following child elements are supported:

| Element                  | Cardinality | Description                                       |
| ------------------------ | ----------- | ------------------------------------------------- |
| `<description>`          | 0 or 1      | Human-readable description of the mapping           |
| `<default_parser>`       | 0 or 1      | Default parser applied to unmapped fields           |
| `<default_date_pattern>` | 0 or 1      | Default date parsing codec for `DateTime` fields    |
| `<timeline>`             | 0 or 1      | Timeline configuration for visualizing records      |
| `<fields>`               | 0 or 1      | Container for field definitions                     |
| Any other element        | 0..N        | Treated as a **parameter** stored in the [`DataTypeMapping.params`](/plugin-creation/api_documentation/#datatypemapping) attribute  |

---

### 2a. `<description>`

A plain text element providing a human-readable description.

```xml
<description>Parse data from the NTFS Info csv file</description>
```

---

### 2b. `<default_parser>`

Specifies which parser to use when an input line does not have a matching field.

| Attribute      | Required | Default    | Allowed Values |
| -------------- | -------- | ---------- | -------------- |
| `value`        | No       | `"Ignore"` | `"String"` or `"Ignore"` |

```xml
<default_parser value="Ignore" />
```

---

### 2c. `<default_date_pattern>`

Specifies the default date/time parsing codec when no explicit qualifier is given.

| Attribute      | Required | Default | Description                                   |
| -------------- | -------- | ------- | --------------------------------------------- |
| `value`        | No       | `"iso"` | Date format specification                      |

Allowed values (from `DateInputCodec::from_str`):
- `"iso"`: ISO 8601 format (e.g., '2023-12-31T23:59:59').
- `"file_time"`: Windows File Time in seconds (e.g., 133210364868558102).
- `"timestamp"`: Unix timestamps in seconds (e.g., 1703654400).
- `"timestamp_hex"`: Unix timestamps in seconds, in hexadecimal format as (e.g., 0x5010ad0a).
- `"timestamp_ms"`: Unix timestamps in milliseconds (e.g., 1704067199000).
- `"timestamp_ns"`: Unix timestamps in nanosecond (e.g., 1703664000123456789). 
- any pattern (e.g. `'%Y-%m-%d %H:%M:%S.%3f'`) that match the chrono [formatting syntax](https://docs.rs/chrono/latest/chrono/format/strftime/index.html)


```xml
<default_date_pattern value="iso" />
<default_date_pattern value='%Y-%m-%d %H:%M:%S.%3f' />
```

---

### 2d. `<fields>`

The central element of the configuration. Contains field definitions that map input data to output fields.

```xml
<fields>
  <field input="FirstName" output="first_name" parser="String" />
  ...
</fields>
```

Supported child elements inside `<fields>`:

| Element          | Description                                   |
| ---------------- | --------------------------------------------- |
| `<field>`        | A single-field mapping                          |
| `<array>`        | An array (repeating) of fields                  |
| `<object>`       | A nested object containing sub-fields            |
| `<multi_input>`  | Joins multiple fields into one output field      |

---

#### 2d-i. `<field>` — Single Field

Maps a single input column/element to an output field.

| Attribute                 | Required | Default    | Description                                    |
| ------------------------- | -------- | ---------- | ----------------------------------------------- |
| `input`                   | **Yes**  | -         | Name of the input field (CSV column, JSON key, etc.) |
| `output`                  | No       | Same as `input` | Name of the output field. If omitted, defaults to the input name |
| `parser`                  | **Yes**  | -          | Name of the parser to apply                      |
| `qualifier`               | No       | -          | A qualifier name that maps to specific parsing behavior |
| `display_name`            | No       | -          | Human-readable display name for the field         |
| `description`             | No       | -          | Additional description of the field               |
| `primary_key`             | No       | `false`    | Marks this field as part of a unique identifier   |
| `default_value`           | No       | -          | Fallback value if the parser returns empty/null   |

**Example:**
```xml
<field input="FirstName" output="first_name" parser="String" />
<field input="radixInt" parser="IntRadix" radix="16" />
<field input="anothersString" parser="StringToUpper" />
<field input="yetAnothersString" parser="StringToLower" />
<field input="ignore_field" parser="Ignore" />
<field input="aFloat" parser="Float" qualifier="FILE_SIZE" />
<field input="someDate" parser="DateTime" qualifier="DATE_CREATION" output="created_date" />
```

---

#### Supported Built-in Parsers

| Parser           | Description                                      | Additional Attributes         |
| ---------------- | ------------------------------------------------ | ----------------------------- |
| `Ignore`         | Skips the field                                   | -                             |
| `String`         | Returns the raw string value                      | -                             |
| `StringToUpper`  | Converts to uppercase                             | -                             |
| `StringToLower`  | Converts to lowercase                             | -                             |
| `Int`            | Parses as 64-bit integer                           | -                             |
| `Float`          | Parses as floating-point number                    | -                             |
| `Bool`           | Parses as boolean                                  | -                             |
| `IntRadix`       | Parses as integer with explicit radix              | `radix` (unsigned int, e.g. `"16"`) |
| `IntToHex`       | Formats an integer as hexadecimal                  | `width` (unsigned int, default `"0"`) |
| `DateTime`       | Parses a date/time string                          | -                             |
| `Dynamic`        | Tries multiple parsers in sequence                  | See below                     |
| `Split`          | Splits a string by a delimiter                      | `split_by` (e.g., `";"`)     |
| `Extension`      | Uses a custom Rust extension parser                 | -                             |
| `PyParser`       | Uses a Python parser extension                     | -                             |

---

#### 2d-ii. `<field>` with Dynamic Parsers

A `<field>` can have `parser="Dynamic"` with nested `<parser>` child elements. The system tries each parser in order until one succeeds.

```xml
<field input="value" parser="Dynamic">
  <parser value="Int" />
  <parser value="Float" />
  <parser value="String" />
</field>
```

This will first try `Int`, then `Float`, then `String`.

---

#### 2d-iii. `<array>` - Repeating Fields

Wraps a single field definition to handle repeating/arrays of values. An `<array>` must contain **exactly one** child element (which itself can be a `<field>`, `<object>`, or `<multi_input>`).

```xml
<!-- Simple repeating field -->
<array>
  <field input="item" parser="String" />
</array>

<!-- Repeating nested object -->
<array>
  <object input="entry" output="entry">
    <field input="name" parser="String" />
    <field input="value" parser="String" />
  </object>
</array>
```

---

#### 2d-iv. `<object>` - Nested Objects

Groups multiple fields into a structured/nested output.

| Attribute | Required | Default | Description                                    |
| --------- | -------- | ------- | ----------------------------------------------- |
| `input`   | **Yes**  | -       | Input name prefix or path                        |
| `output`  | No       | Same as `input` | Output path prefix                     |
| `qualifier` | No     | -       | Qualifier for the object                          |
| `display_name` | No  | -       | Display name                                      |
| `description`  | No  | -       | Description                                       |
| `ignore`  | No       | `"false"` | If `"true"`, skip all fields inside this object  |

```xml
<object input="LinkInfo" output="link" parser="String" >
  <field input="TargetPath" output="target" parser="String" />
  <field input="DisplayName" output="display" parser="String" />
  <field input="RelativePath" output="relative" parser="String" />
</object>
```

Objects can be nested arbitrarily deep.

---

#### 2d-v. `<multi_input>` - Joining Multiple Inputs

Combines multiple input fields into a single output field, using a specified join behavior.

| Attribute                      | Required | Default   | Description                                        |
| ----------------------------- | -------- | --------- | --------------------------------------------------- |
| `output`                      | **Yes**  | -         | Output field name                                    |
| `parser`                      | **Yes**  | -         | Must be `"Join"`                                     |
| `separator`                   | **Yes**  | -         | String to join the values with (e.g., `"\\"`)        |
| `avoid_separator_duplication` | No       | `"true"`  | When `true`, collapses consecutive separator characters |
| `qualifier`                   | No       | -         | Qualifier name                                       |
| `display_name`                | No       | -         | Display name                                         |
| `description`                 | No       | -         | Description                                          |

Children are field definitions whose values get joined.

```xml
<multi_input output="file_path" qualifier="FILE_PATH" parser="Join" separator="\"
  avoid_separator_duplication="true">
  <field input="ParentName" parser="String" default_value="\" />
  <field input="File" parser="String" />
</multi_input>
```

---

## 3. `<timeline>` Element

Defines how records are displayed in a timeline view. 

```xml
<timeline>
  <timeline_type value="Standard" />
  <max_date_meaning value="0" />
  <related_user>
    <output_name value="system.security.user_id" />
  </related_user>
  <description include_field_name="false" field_separator=":">
    <output_name value="system.provider.provider_name" />
    <output_name value="system.event_id" />
  </description>
  <additional_description>
    <conditional>
      <condition path="system.event_id" value="123" parser="Int"/>
      <output_name value="system.computer" />
    </conditional>
    <otherwise>
      <output_name value="system.event_record_id" />
    </otherwise>
  </additional_description>
</timeline>
```

| Element                    | Cardinality | Description                                   |
| -------------------------- | ----------- | ----------------------------------------------- |
| `<timeline_type>`          | **1**        | Type of timeline rendering                       |
| `<max_date_meaning>`       | 0 or 1       | number of different 'date meaning' displayed when several fields are at the same date       |
| `<related_user>`           | 0 or 1       | Related user output path                         |
| `<description>`            | 0 or 1       | Primary description fields                       |
| `<additional_description>` | 0 or 1       | Secondary description with conditional logic      |

### 3a. `<timeline_type>`

| Attribute | Required | Allowed Values       |
| --------- | -------- | -------------------- |
| `value`   | **Yes**  | `"Standard"` or `"MacbMacb"` |

```xml
<timeline_type value="Standard" />
<timeline_type value="MacbMacb" />
```

The `MacbMacb` value provides a compact representation for the folowing fields output names:   
- `si_lastmod_date`
- `si_lastaccess_date`
- `si_lastchange_date`
- `si_creation_date`
- `fn_lastmod_date`
- `fn_lastaccess_date`
- `fn_lastchange_date`
- `fn_creation_date`

### 3b. `<max_date_meaning>`

| Attribute | Required | Description                            |
| --------- | -------- | -------------------------------------- |
| `value`   | **No**  | number of different 'date meaning' displayed when several fields are at the same date |

```xml
<max_date_meaning value="0" />
```

### 3c. `<related_user>`

Specify a field that contains related user primary information.

```xml
<related_user>
  <output_name value="system.security.user_id" />
</related_user>
```

### 3d. `<description>`

Defines the primary description shown for each timeline entry.

| Attribute               | Required | Default  | Description                                   |
| ----------------------- | -------- | -------- | ----------------------------------------------- |
| `include_field_name`    | No       | `"true"` | Whether to include the field name in output     |
| `field_separator`       | No       | `" - "`  | Separator between field name and value           |

Children: zero or more `<output_name>` elements.

```xml
<description include_field_name="false" field_separator=":">
  <output_name value="system.provider.provider_name" />
  <output_name value="system.event_id" />
</description>
```

### 3f. `<additional_description>`

Defines secondary description fields with optional conditional logic.

| Attribute               | Required | Default  | Description                                   |
| ----------------------- | -------- | -------- | ----------------------------------------------- |
| `include_field_name`    | No       | `"true"` | Whether to include field names                  |
| `field_separator`       | No       | `" - "`  | Separator between field name and value           |

Supported children:

| Element              | Cardinality | Description                                     |
| -------------------- | ----------- | ----------------------------------------------- |
| `<output_name>`      | 0..N        | Always-included additional description field      |
| `<conditional>`      | 0..N        | Conditional additional description                |
| `<otherwise>`        | 0 or 1      | Fallback additional description                  |

```xml
<additional_description include_field_name="true" field_separator=" - ">
  <!-- Always shown -->
  <output_name value="file_size" />

  <!-- Conditionally shown -->
  <conditional>
    <condition path="system.event_id" value="123" parser="Int"/>
    <condition path="system.provider.provider_name" value="provider" parser="String"/>
    <output_name value="system.computer" />
    <output_name value="system.event_record_id" />
  </conditional>

  <!-- Fallback -->
  <otherwise>
    <output_name value="default_description" />
  </otherwise>
</additional_description>
```

#### `<conditional>`

Contains one or more `<condition>` elements. The additional description fields within are only shown when **all** conditions match.

| Attribute              | Required | Description                                 |
| ---------------------- | -------- | -------------------------------------------- |
| `path`                 | **Yes**  | Full dotted output path for the field being checked |
| `value`                | **Yes**  | Expected value(s), pipe-separated for OR logic |
| `parser`               | **Yes**  | Parser to use for value comparison             |

```xml
<conditional>
  <!-- Match if event_id is 123 OR 421 OR 1433 -->
  <condition path="system.event_id" value="123|421|1433" parser="Int"/>
  <!-- AND provider is "provider1" OR "provider2" -->
  <condition path="system.provider.provider_name" value="provider1|provider2" parser="String"/>

  <!-- These fields are shown when the conditions match -->
  <output_name value="system.computer" />
  <output_name value="system.event_record_id" />
</conditional>
```

#### `<otherwise>`

Provides fallback fields shown when no `<conditional>` matches.

```xml
<otherwise>
  <output_name value="fallback_description_field" />
</otherwise>
```

---

## 4. Arbitrary Parameters

Any element inside `<mapping>` that is not one of the recognized elements (`timeline`, `fields`, `description`, `default_parser`, `default_date_pattern`) is treated as a named parameter and stored in a dictionary accessible via the.
[`DataTypeMapping.params`](/plugin-creation/api_documentation/#datatypemapping) attribute

```xml
<mapping data_type="my_data">
  <csv_delimiter value="," />
  <max_rows value="10000" />
  <custom_param value="some_value" />
</mapping>
```

In this example, `csv_delimiter`, `max_rows`, and `custom_param` are in the `params` dictionary.

---
