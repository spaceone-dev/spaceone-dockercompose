# 🚀 SpaceONE Docker-Compose Installer

> a [SpaceONE](https://github.com/spaceone-dev) docker-compose to deploy [SpaceONE](https://github.com/spaceone-dev) on Docker. 

Manage your infrastructure with SpaceONE. It doesn't matter what your infrastructure is based on. SpaceONE supports AWS, GCP, Azure, IDC, ...etc.

![preview](https://helm.stargate.spaceone.dev/media/preview.png)

# ⭐️ Installation

This installation is for developer only.

### Requirements

* `docker`
* `docker-compose` 

### Commands

You should update environment variables at build-data/environment/debug.mk

```
############################
# Docker Image Registry
#############################
IMAGE_REGISTRY=spaceone
VERSION=latest

############################
# Update Your environment
# - supervisor (private ip address of this machine)
# MacOS
#SUPERVISOR_HOSTNAME=$(shell ipconfig getifaddr en0)
# Linux
SUPERVISOR_HOSTNAME=$(shell hostname -i)

############################
# Service List
############################
BACKEND = identity secret repository inventory plugin
FRONTEND = console console-api
SUPERVISOR = supervisor
TESTER = tester

############################
# Running List
############################
RUN_MONGODB = y
RUN_REDIS = y
RUN_VAULT = y
RUN_CONSUL = y
RUN_BACKEND = y
RUN_FRONTEND = y
RUN_SUPERVISOR = y
RUN_TESTER = y
```

In the repository root directory, install SpaceONE.

```bash
$ make all
```


### 1. Update DNS for web browser access.

edit your hosts file for access.

In Linux PC or MacOS, edit /etc/hosts
In Windows PC, edit c:\windows\system32\drivers\etc\hosts

```
#
# Elastic IP address, if you installed at EC2 instance.
# <EC2 EIP> root
# If you use MacOS, use 127.0.0.1
127.0.0.1 root
```

You can see the console page via http://root:8280

## Development guides

This will be appended soon.

## Configurations

This will be appended soon.

## Release History

- 0.1.0
  - Initial version.

## Contributing

1. Fork it (https://github.com/spaceone/spaceone-dockercompose)
2. Create your branch (`git checkout -b foo`)
3. Commit your changes
4. Push to your branch
5. Create a new Pull Request (https://github.com/spaceone/spaceone-dockercompose)
