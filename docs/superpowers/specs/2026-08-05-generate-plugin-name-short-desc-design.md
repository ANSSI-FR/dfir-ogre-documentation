# Rework `generate_plugin_doc.py` to use `<name>` and `<short_description>`

Date: 2026-08-05

## Context

The XML plugin definitions (in `dfir-ogre-plugin-windows/configuration`) now give each
`<mapping>` a unique `<name>` and a `<short_description>`. All 85 mappings provide both,
and the names are unique (85 mappings, 85 unique names).

The generator script (`dfir-ogre-documentation/script/generate_plugin_doc.py`) currently
derives the display title and file name from `data_type`, and the card subtitle from the
first sentence of the long `<description>`. Because some `data_type` values are shared
across plugins (e.g. `browser_download_history` for Chrome and Firefox,
`amcache_program_xml` for three plugins), the script resorts to messy disambiguation
(`link_set` + `last_camel_case_word`) producing titles like "Amcache Program Xml XML".
Using the unique `<name>` removes this entire workaround.

## Goal

- Display title and file/link name come from `<name>`.
- Card subtitle comes from `<short_description>`.

## Design

### 1. Data flow (main loop)

For each `<mapping>`, read three things:

- `<name>` -> display title and slug source.
- `<short_description>` -> card subtitle.
- `<description>` (the long one) -> doc page body, **unchanged**.

`Document` gains a `name` field. The old subtitle derivation
(`description.split(".")[0]`) and the `title`-mangling are removed.

### 2. Title & file/link naming

- Title = raw `<name>` (e.g. "Processes Orc V1", "X509Cert Software", "Prefetch").
- File name / link = slug of `<name>`: lowercase, non-alphanumeric to `_`, trimmed
  (e.g. "Chrome Download History" -> `chrome_download_history`).
- Delete the `link_set` / `last_camel_case_word` disambiguation hack and the
  `win_` / title-case mangling — no longer needed since slugs are unique for unique names.

Options considered: lowercase-with-underscores (chosen, keeps current URL style and
minimal churn) vs lowercase-with-hyphens.

### 3. Cards

- `subtitle` = `<short_description>` (replaces `description.split(".")[0]`).
- Card layout otherwise unchanged.

### 4. Unchanged

- `data_type` + `parser` in the "Data Type / Python Parser" callout.
- Category grouping, `_index.md` structure, fields/timeline parsing.

### 5. Defensive guard

Verified: 85 distinct names -> 85 distinct slugs (zero collisions). Still assert slug
uniqueness and, on a future collision, append the `data_type` as a disambiguator rather
than silently overwriting.

## Acceptance criteria

- Running the script produces one `.md` page per `<name>`, named from the slug, with
  front-matter title = `<name>`.
- Cards show `<name>` as title and `<short_description>` as subtitle.
- No duplicate links / no disambiguation "XML" suffixes.
- `data_type` + `parser` still shown in the callout.
- Generated docs render in hugo without broken links.
</content>
