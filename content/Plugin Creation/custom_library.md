---
date: '2026-01-06T15:54:09+01:00'
title: 'Creating a custom library'
cascade:
  type: docs
  params:
    breadcrumbs: true
weight: 1
---

While we strongly encourage you to contribute to DFIR‑OGRE by submitting new plugins, we recognize that some plugins may need to remain private.

A custom library makes sense if you need to create [custom Python parsers](/plugin-creation/custom_parsers/)  that you don't want to share.

This guide describes how to create a separate project to develop a private plugin library.
{{% steps %}}


## Check Prerequisites

| Item | Minimum version |
|------|-----------------|
| **Python** | 3.10 or newer |
| **git** | any recent version |
| **uv** | ≥ 0.4 (installable with `pip`)


## Initialize project

```bash
uv init --package my-secret-plugins

cd my-secret-plugins
# add the dfir-ogre-common dependency
uv add  "dfir-ogre-common @ git+ssh://git@github.com/ANSSI-FR/dfir-ogre-common.git"

# create folder that will contains the XML descriptors
# it is the same as the one defined in dfir-ogre-plugin-windows
mkdir configuration

# create the same test folder as the one defined in dfir-ogre-plugin-windows
mkdir tests

# install ogre to be able to test your plugins
git clone git@github.com/ANSSI-FR/dfir-ogre.git
uv pip install ./dfir-ogre

```
{{< callout >}}
  The installation takes some time because it compiles some Rust and C code.
{{< /callout >}}

After this step the layout should looks like:
{{< filetree/container >}}
  {{< filetree/folder name="my-secret-plugins" >}}
    {{< filetree/folder name=".git" state="closed" />}}
    {{< filetree/folder name=".venv" state="closed" />}}
    {{< filetree/folder name="configuration" state="closed" />}}
    {{< filetree/folder name="src" state="open" >}}
      {{< filetree/folder name="my_secret_plugins" state="open" >}}
        {{< filetree/file name="\_\_init\_\_.py" >}}
      {{< /filetree/folder >}}
    {{< /filetree/folder >}}
    {{< filetree/folder name="tests" state="closed" />}}
    {{< filetree/file name=".gitignore"  >}}
    {{< filetree/file name="README.md"  >}}
    {{< filetree/file name="pyproject.toml"  >}}
    {{< filetree/file name="uv.lock"  >}}
  {{< /filetree/folder >}}
{{< /filetree/container >}}

### Create a test plugin

In the `configuration` folder create your first [plugin descriptor](/plugin-creation/xml_descriptor) 

```xml {filename="configuration/dummy_plugin.xml"}
<?xml version="1.0" encoding="UTF-8"?>
<plugin parser="Merge" file_encoding="UTF_8">
  <mapping data_type="dummy" />
</plugin>
```

This plugin will use the python `Merge` parser to read a UTF-8 file and merge every line into a single artefact of the `dummy` datatype.

## Test the plugin

Find a text file you want to merge and run the following command:

```bash
dfir-ogre plugin \
    --filename my_text_file.txt \
    --plugin_config configuration/dummy_plugin.xml \
    --computer_name SAMPLE_HOST \
    --output_folder ouput/ \
```

it should create a new file in the `output/` folder

{{< callout >}}
  Congratulation! you have created your first plugin!
{{< /callout >}}

{{% /steps %}}
