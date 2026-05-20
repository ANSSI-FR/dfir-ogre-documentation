---
date: '2026-01-06T15:54:09+01:00'
title: 'Parser Tutorial'
cascade:
  type: docs
  params:
    breadcrumbs: true
weight: 1
---

A parser is a simple python class that extends the abstract class `OgrePlugin` and must implements two methods

```python {filename="src/my-secret-plugins/hello_world.py"}
[...]
class HelloWorld(OgrePlugin):
    def description(self) -> PluginDescription:...
      """
      Returns a `PluginDescription` with two strings: 
      - command: used to identify the plugin in the XML descriptor
      - description: str
      """


    def parse(
        self,
        input_file: str,
        plugin_file: str,
        run_config: RunConfiguration,
        metadata: Metadata,
    ) -> RunReport:
      """
      Implement the parsing logic and write artefacts. 
      I takes the following parameters:
        - `input_file`: the file that will be parsed
        - `plugin_file`: the file name of the XML decriptor
        - `run_config`: the output configuration and additional parameters.
                        comes from the `ogre.yaml` file or `CLI parameters`
        - `metadata`: some metadata about the file being parsed
      """
```
---

## Sample Dataset

Before starting, let's create our sample file :

```{filename="sample_names.txt"}
John Doe  
Jane Doe  
Jack Doe  
Jill Doe
```
We will create a parser that reads each line and output a greetings artefact

---

## The Hello World parser


Let's create the mandatory "Hello World" parser in the `src/my-secret-plugins/hello_world.py`
```python {filename="src/my-secret-plugins/hello_world.py"}
from dfir_ogre_common import (
    Metadata,
    OgrePlugin,
    Output,
    PluginConfiguration,
    PluginDescription,
    Record,
    RunConfiguration,
    RunReport,
    Value,
)
class HelloWorld(OgrePlugin):
    def description(self) -> PluginDescription:
        return PluginDescription(
            "Greetings", "The mandatory hello world tutorial"
        )

    def parse(
        self,
        input_file: str,
        plugin_file: str,
        run_config: RunConfiguration,
        metadata: Metadata,
    ) -> RunReport:
        # 1. Load plugin-specific configuration
        plugin_config = PluginConfiguration.load(plugin_file)
        
        # 2. Create a RunReport to capture errors/warnings
        report = RunReport()
        
        # 3. Open the output context manager
        with Output(run_config, plugin_config, metadata) as output:
          try:
            # 4. Open the input file and parse it
            with open(input_file) as input:
              
              for line in input:
                  # 5. Build a Record for each entity found
                  record = Record()
                  record.add("greeting", Value.String(f"Hello {line.strip()} !)"))
                  
                  # 6. Write the record through the Output context manager
                  output.write(record)
                  
          except Exception as e:
            # 7. add any errors to the report
            report.add_error(f"{e}")
            
         # 8. Finally, merge output's internal report into the final report
        report.add_output_report(output.get_report())
        return report
```
Key points:
- A `Record` is a [key-value dictionnary](/plugin-creation/custom_parsers/api_documentation/#record), used to represent an artefact in the data model.
- Records only accept `Value` data, which represents [various serializable](/plugin-creation/custom_parsers/api_documentation/#value) data types.

## Export your plugin

Plugins must be exported by the root `__init__.py` be able to be discovered by DFIR-OGRE
```python {filename="src/my-secret-plugins/__init__.py"}

from .hello_world import HelloWorld

```
{{< callout >}}
It is very easy to forget this part when creating plugins
{{< /callout >}}

## Create a plugin with the XML descriptor

The minimal plugin required to use the hello world parser. 

```xml {filename="configuration/hello_world.xml"}
<?xml version="1.0" encoding="UTF-8"?>
<plugin parser="Greetings" file_encoding="UTF_8">
  <mapping data_type="hello_world">
    <fields>
    </fields>
  </mapping>
</plugin>
```

`parser="Greetings"` references the *PluginDescription.command* returned by the `HelloWorld.description()` method.
{{< callout >}}
If you want to use the [csv output format](/usage/ogre_configuration/#parameters), you will have to reference the `greeting` field in the `<fields>` section.
{{< /callout >}}


## Testing the plugin


```bash
## assuming that you have created a project named my-secret-plugins
uv pip install .
dfir-ogre plugin \
    --filename sample_names.txt \
    --plugin_config configuration/hello_world.xml \
    --computer_name SAMPLE_HOST \
    --output_folder ouput/ \
    --library my_secret_plugins
```

Key points:
- the `library` will tell le program to load the **`my_secret_plugins`** packages to find classes that implements the OgrePlugin

{{< callout >}}
It is `my_secret_plugins` not `my-secret-plugins`!
{{< /callout >}}

## Deploying the plugin in an `ogre.yaml` file

{{% steps %}}

 ### Install your python package
 
 Make sure that you plugin package is installed alongside DFIR-OGRE.

 ### Reference your package
 
 Edit the ogre.yaml file to reference your custom python package
 ```yaml {filename="ogre.yaml"}
plugin_prefixes:
    - dfir_ogre_plugin
    - my_secret_plugins
    
  # [...]the rest of the configuration [...] 
```
 
### Copy the XML descriptor
 
Put the `hello_world.xml` file in the folder referenced by the `plugin_folder` folder parameter.
It is best to put it in a dedicated subfolder like (ex. `myplugins`)


### Edit the mapping section 

```yaml {filename="ogre.yaml"}
mapping:
    # Hello world Greetings
    - original_file_pattern: '.*\\.*_names.txt$'
      plugin_file: $plugin_folder/myplugins/hello_world.xml
      mapping_label: some_greetings
      output:
          - raw_data
  
    # ActivityCache
    - original_file_pattern: '.*\\ActivitiesCache.db$'
      plugin_file: $plugin_folder/activity_cache.xml
      mapping_label: activity_cache
      output:
          - timeline

     # [...]the rest of the configuration [...] 
```
{{% /steps %}}
