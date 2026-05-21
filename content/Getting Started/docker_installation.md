---
date: '2026-01-06T15:52:05+01:00'
title: 'Docker‑based Installation'
weight: 1
---


A multi‑stage Dockerfile is provided under `dfir-ogre/docker/Dockerfile`. It builds the **DFIR-OGRE** packages from the source and ships a minimal runtime image.

This is the recommended way to use **DFIR-OGRE** as it allows for finer control of ressources usage than the manual installation.

## Building the Docker image  

Run the following command to create a `dfir-ogre:latest` image
```bash
git clone https://github.com/ANSSI-FR/dfir-ogre.git
cd dfir-ogre/docker
./build.sh
```

## Usage example

```bash
# Creates a data and tmp folder 
mkdir data
mkdir tmp

# Put the ogre.yaml configuration file in /data/
cp _your_source_path_/dfir-ogre/configuration/ogre_docker.yaml data/ogre.yaml

# Put your ORC achives in data/input 
docker run \
        -u $(id -u):$(id -g) \
        -v ./data:/data  \
        -v ./tmp:/tmp/ogre  \
        --rm \
        --memory=8g \
        --memory-swap=8g \
        --log-opt max-size=10m \
        --log-opt max-file=1 \
        dfir_ogre:latest \
        orc \
        --configuration /data/ogre.yaml \
        --archive '/data/input/ORC_WorkStation_xxx_Outcome.json'
```

{{< callout >}}
- for details on the **ogre.yaml**, see the [configuration guide](/usage/ogre_configuration/)
- for a full list of supported command‑line options, consult the [command‑line usage page](/usage/command_line_usage/).
{{</ callout >}}


### Docker Options
| Option | What it does |
|--------|--------------|
| `--rm` | **Auto‑remove** : automatically delete the container when it exits. A new clean container is created for every `dfir-ogre` run |
| `-u $(id -u):$(id -g)` | **User/Group ID** : runs the container as the current host user and group. Prevents files created inside the container from being owned by `root` on the host, making permission handling easier when mounting volumes. |
| `-v ./data:/data` | **Volume bind‑mount** : maps the host directory `./data` into the container at `/data`. Gives the container access to persistent data |
| `-v ./tmp:/tmp/ogre` | **Second bind‑mount** : maps `./tmp` on the host to `/tmp/ogre` inside the container. Provides a writable temporary space specific to the application. Usefull for debugging |
| `--memory=8g` | **Memory limit** : caps the container’s RAM usage at 8 GB. Protects the host from a runaway plugin that could otherwise consume all system memory. |
| `--memory-swap=8g` | **Swap limit** : sets the total memory + swap that the container may use to 8 GB (i.e., disables swap). Guarantees the container cannot start swapping, which could degrade performance. |
| `--log-opt max-size=10m` | **Log rotation max size** : when a container’s log file reaches 10 MiB, rotates it. Prevents a runaway plugin to fill up disk space with logs. |
| `--log-opt max-file=1` | **Log rotation max files** : keep only the most recent log file (the current one) and discard older ones. Together with `max-size`, this ensures a single ~10 MiB log file at most |
