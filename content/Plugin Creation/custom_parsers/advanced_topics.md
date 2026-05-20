---
date: '2026-01-06T15:54:09+01:00'
title: 'Advanced topics'
cascade:
  type: docs
  params:
    breadcrumbs: true
weight: 2
---

## Using field definition

In the [hello world tutorial](/plugin-creation/custom_parsers/hello_world/), data is inserted in the records using 
```python {filename="src/my-secret-plugins/hello_world.py"}
record.add("greeting", Value.String(f"Hello {line.strip()} !)")
```

This is convenient for simple datasets, but if you data is complex with nested three strutuctures, it can be easier to declare the datamodel in the XML descriptor, and use it in you code to build the records.

Lets consider the fields definition in an XML plugin descriptor:
```xml {filename="configuration/some_plugin.xml"}
...
<fields>
      <field input="type" parser="String" />
      <field input="size" parser="Int" />
      <field input="modification_time" parser="DateTime" />
      <object input="header">
        <field input="size" parser="Int"/>
        <!-- Input data is like flag1,flag2,flag3  and we want to convert it ot an array-->
        <field input="flags" parser="Split" split_by=","/>
      </object>
<fields>
...
```

Here is how to use the data model in you python code:
```python {filename="src/my-secret-plugins/some_plugin.py"}
def parse(
    self,
    input_file: str,
    plugin_file: str,
    run_config: RunConfiguration,
    metadata: Metadata,
) -> RunReport:
    # 1. Load plugin-specific configuration
    plugin_config = PluginConfiguration.load(plugin_file)
    # 2. get the parsers built from the <fields>
    parsers = plugin_config.get_parsers()
    
    # ... 
              
              record = Record()
              #returns None if the field "type" does not exists
              type_p = parsers.get_parser("type")
              if type_p:
                type_p.parse("some_type", record)
                
              size_p = parsers.get_parser("size")
              if type_p:
                type_p.parse("1024", record)
              
              # handle the header object
              header_record = Record()
              
              # retrieve the parsers for the header object
              header_parsers = parsers.get_parser_subtree("key")
              if header_parsers:
                flags_p = header_parsers.get_parser("flags")
                if flags:
                  # parse data into the header record
                  flags_p.parse("flag1,flag2,flag3", header_record)
                
                size_p = header_parsers.get_parser("size")
                if size_p:
                  size_p.parse("123", header_record)
              
              # finaly add the header record to the main artefact
              record.add("header", Value.Object(header_record))
              
              
              output.write(tuple)
    # ...         

```

---

## Batched Plugins

The `OgrePlugin` abstract class allows you to create plugins that parses one file. It is sufficient for most of the case but in some situation you might want to be able to parse several files:
- for performance reason: the plugin initialisation has a cost and if you have a lot of small file to parse, it is more efficient to process them in one batch.
- for complex scenario: you parser might need two different files to extract the artefacts

In those cases, your parser can extends the `OgreBatchedPlugin`, that provides multiple input file.

```python {filename="src/my-secret-plugins/batched_plugin.py"}
class MyBatchedPlugin(OgreBatchedPlugin):
    def description(self) -> PluginDescription:
        return PluginDescription("MyBatch", "batch usage example")

    def parse(
        self,
        input_files: List[BatchEntry],
        plugin_file: str,
    ) -> RunReport:
      ...
      
      
```

`BatchEntry`: contains the necessary data to parse each files:     
- `file`: the file that will be parsed.
- `run_config`:  the output configuration and additional parameters.
- `metadata`: some metadata about the file being parsed.
    
{{< callout type="warning" >}}
In the XML descriptor, you *MUST* put add `batch="true"`, otherwise, the parser will not be detected and an error will be returned. 
{{< /callout >}}

```xml {filename="configuration/batched_plugin.xml"}
<?xml version="1.0" encoding="UTF-8" ?>
<plugin parser="Batched" batch="true" file_encoding="UTF_8">
  <mapping data_type="batched">
    <!-- ... -->
  </mapping>
</plugin>
```
---

If you configure your `ogre.yaml` file to use a batched parser, DFIR-OGRE will collect every file that match the pattern and call the `parse(...)` function once.

```yaml {filename="ogre.yaml"}
mapping:
    # Batched Hello world
    - original_file_pattern: '.*\\.*_names.txt$'
      plugin_file: $plugin_folder/myplugins/batched_plugin.xml
      mapping_label: batched
      output:
          - raw_data
     # [...]the rest of the configuration [...] 
```
{{< callout type="warning" >}}
Currently, the batch plugins are only supported by  the `orc` and `timeline` commands. It does not work with `plugin`.
{{< /callout >}}
