---
date: '2026-01-06T15:54:09+01:00'
title: 'Api Documentation'
cascade:
  type: docs
  params:
    breadcrumbs: true
weight: 5
---

This documentation provides a high level overview of the core API components provided by the `dfir-ogre-common` library.

---


## 📊 Data Models

Core structures used to represent parsed data in a generic format.

### `Record`
A wrapper for key-value pairs, primarily used to represent objects in the data model.

**Methods:**
- `__init__()`: Initializes an empty record.
- `add(name: str, value: Value)`: Adds a field and its associated value.
- `clear()`: Removes all entries from the record.
- `len() -> int`: Returns the number of fields in the record.
- `to_string() -> str`: Returns a string representation of the record.

### `Value`
A polymorphic type representing various serializable data types.

**Static Factory Methods:**
- `Null()`: Represents a null value.
- `String(v: str)`: Represents a string.
- `Array(v: List[Value])`: Represents a list of `Value` objects.
- `Int(v: int)`: Represents an integer.
- `Float(v: float)`: Represents a floating-point number.
- `Bool(v: bool)`: Represents a boolean.
- `Date(v: datetime)`: Represents a UTC timestamp.
- `Object(v: Record)`: Represents a nested `Record`.

---


## 🔍 Parsing

These classes define the interface and configuration for creating and managing Ogre plugins.

### `OgrePlugin`
A minimal base class for plugins, allowing custom parsing logic to be implemented in Python.

**Methods:**
- `description() -> PluginDescription`: Returns a `PluginDescription` object containing human-readable details about the plugin.
- `parse(input_file: str, plugin_file: str, run_config: RunConfiguration, metadata: Metadata) -> RunReport`: The core entry point for parsing. Processes the `input_file` using the provided configuration and metadata.

### `OgreBatchedPlugin`
This class extends the plugin pattern to handle [batched input](/plugin-creation/custom_parsers/advanced_topics/#batchedplugins).

**Methods:**
- `description() -> PluginDescription`: Returns a `PluginDescription` object containing human-readable details about the plugin.
- `parse(self, input_files: List[BatchEntry], plugin_file: str) -> RunReport`: Execute the parsing logic for the given batch of input files.


### `RunConfiguration`
Holds all parameters required to execute parsing operations. It is passed as a parameter of the `OgrePlugin.parse(...)` method and can be be instanciated manually for testing purposes (e.g: in unit tests)

**Methods:**
- `__init__(output: List[OutputConfiguration], force_snake_case: bool = False, params: Optional[Dict[str, Optional[str]]] = None)`


### `PluginConfiguration`
Manages all field mappings available for a specific plugin. It is generaly created at the very beginning of a parser, using the plugin_file parameter passed in the `parse() function

```python
parse(input_file: str, plugin_file: str, run_config: RunConfiguration, metadata: Metadata) -> RunReport:
  plugin_config = PluginConfiguration.load(plugin_file)
  parsers = plugin_config.get_parsers()
```

**Methods:**
- `load(input_file: str, python: Optional[Dict[str, Any]] = None, extension: Optional[Dict[str, ParserExtension]] = None) -> PluginConfiguration`: Class method to load a configuration from a file.
- `get_parsers(data_type: Optional[str] = None) -> Optional[FieldParserTree]`: Returns the `FieldParserTree` for the specified data type. If `data_type` is `None`, the first configured data type is returned.
- `get_data_type_mapping(self, data_type: Optional[str] = None) -> DataTypeMapping`: Returns the `DataTypeMapping` for the specified data type.

### `FieldParserTree`
Organizes field parsers into a hierarchical structure, supporting nested path-based access and fallback parsing.
It is returned byt the `PluginConfiguration.get_parsers(..)` method

**Methods:**
- `get_parser(input_name: str) -> Optional[FieldParser]`: Retrieves a parser for a specific field name. Does not support nested paths.
- `get_parser_by_path(path: List[str]) -> Optional[FieldParser]`: Retrieves a parser for a nested field path (e.g., `["System", "TimeCreated"]`).
- `get_parser_subtree(input_name: str) -> Optional[FieldParserTree]`: Retrieves a nested `FieldParserTree` for a specific field, allowing recursive parsing of hierarchical data.
- `get_output_name() -> str`: Returns the output name for the tree.

### `FieldParser`
Manages the parsing of input fields. It encapsulates the logic for extracting and transforming data from a specific input field. It is returned by `FieldParserTree.get_parser...` methods

**Methods:**
- `parse(input: Optional[str], output: Record) -> None`: Parses the input string using registered fields and populates the provided `Record` with the results.
- `parse_into_value(input: Optional[str]) -> Optional[Value]`: Parses the input string and returns the first non-None `Value` found.
- `set_value(value: Value, output: Record) -> None`: Sets a specific `Value` into the output `Record` using the correct associated name.
- `input_name() -> str`: Returns the name of the input field associated with this parser.

### `BatchEntry`
That references a file that will be parsed by an `OgreBatchPlugin`

**Attributes:**
- `file: str` : the file that will be parsed.
- `run_config: RunConfiguration`: the output configuration and additional parameters.
- `metadata: Metadata`:  some metadata about the file being parsed.

### `DataTypeMapping`
This class defines the mapping data for a specific data type

**Attributes:**
- `file_encoding: Optional[str]`: input file encoding
- `params: Dict[str, str]` : additional paramaters defined in the XML descriptor `mapping` section.

### `PluginDescription`
Provides metadata about a plugin's purpose and usage, typically for CLI tools.

**Methods:**
- `__init__(command: str, description: str)`: Initializes the description with a command name and a human-readable description.
- `get_command() -> str`: Returns the command name used to invoke the plugin.
- `get_description() -> str`: Returns the human-readable description.

---

### `RunReport`
Summarizes the results of a parser execution.
**Methods:**
- `__init__()`
- `add_error(error: str)`: Logs an error to the report.
- `add_output_report(output_report: OutputReport)`: Adds an `OutputReport` to the results.

### `Output`
The main handler for writing parsed data to various destinations.

**Methods:**
- `__init__(run_config: RunConfiguration, plugin_config: PluginConfiguration, metadata: Metadata, data_type: Optional[str] = None)`
- `get_report() -> OutputReport`: Retrieves information about the files that have been written.
- `write(data: Record)`: Writes a `Record` of parsed values to all configured destinations.

---

## 🔑 Windows Registry

Classes for interacting with and extracting data from Windows Registry hives.

### `Registry`
Represents a registry hive.

**Methods:**
- `load(input_file: str, root_name: str) -> Registry`: Class method to load a registry hive from a file.
- `glob_keys(path: str) -> List[RegKey]`: Searches for keys matching a glob pattern.

### `RegKey`
Represents a specific registry key and its associated values.

**Attributes:**
- `mtime: datetime`: Last modification time.
- `security_descriptor: SecurityDescriptor`: The key's security descriptor.
- `path: str`: Full path to the key.
- `name: str`: Name of the key.

**Methods:**
- `sub_keys() -> List[RegKey]`: Returns all immediate subkeys.
- `sub_key(path: str) -> Optional[RegKey]`: Gets a specific subkey by name.
- `sub_path(path: str) -> Optional[RegKey]`: Gets a subkey by its relative path.
- `sub_glob(path: str) -> List[RegKey]`: Returns subkeys matching a glob pattern.
- `value(name: str) -> Optional[RegValue]`: Gets a specific registry value by name.
- `values() -> List[RegValue]`: Returns all values in the key.
- `value_data(name: str, default: Optional[Any] = None) -> Optional[Any]`: Gets the raw data of a specific value.
- `to_record() -> Record`: Converts the registry key and its properties into a `Record`.

### `RegValue`
Represents an individual registry value.

**Methods:**
- `name() -> str`: Returns the name of the value.
- `type() -> str`: Returns the data type as a string.
- `data() -> Any`: Returns the value data as a Python object.
- `to_record() -> Record`: Converts the registry value into a `Record`.

---
