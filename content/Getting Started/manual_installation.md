---
date: '2026-01-06T15:52:05+01:00'
title: 'Manual Installation'
weight: 2
---

{{< callout type="important" >}}
DFIR-OGRE has only been tested on Debian systems and does not work on Windows.
A [Docker installation](/getting-started/docker_installation/ "Docker installation") procedure is available to ensure better portability. 
{{< /callout >}}

This manual installation method is intended for debugging or custom plugin development, as it offers less control over resource usage compared to the Docker‑based installation.

---

{{% steps %}}

### Check Prerequisites

| Item | Minimum version |
|------|-----------------|
| **Python** | 3.10 or newer |
| **git** | any recent version |
| **uv** | ≥ 0.4 (installable with `pip`)


### Clone the required repositories

```bash
# Choose a location where you keep all the sources
mkdir -p ~/dfir-ogre && cd ~/dfir-ogre

git clone git@github.com:ANSSI-FR/dfir-ogre-plugin-windows.git
git clone git@github.com:ANSSI-FR/dfir-ogre.git

#create the virtual environment
uv venv 
uv pip install ./dfir-ogre

# Activate the virtual environment
source .venv/bin/activate
```

The prompt should now show the venv name, e.g. `(dfir-ogre) $`.

and the `dfir-ogre` command should be available
```bash
dfir-ogre --help 
```
{{< callout >}}
  The installation takes some time because it compiles some Rust and C code.
{{< /callout >}}

{{% /steps %}}

## Usage example

Extract a DFIR-ORC archive from its Outcome.json file, using the ogre.yaml configuration.

```bash
dfir-ogre orc \
    --archive ORC_xxx_Outcome.json \
    --case sample_case \
    --configuration dfir-ogre/configuration/ogre.yaml
```
{{< callout >}}
- for details on the **ogre.yaml**, see the [configuration guide](/usage/ogre_configuration/)
- for a full list of supported command‑line options, consult the [command‑line usage page](/usage/command_line_usage/).
{{</ callout >}}
