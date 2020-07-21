# 🚀 SpaceONE Docker-Compose Installer

> a [SpaceONE](https://github.com/spaceone-dev) docker-compose to deploy [SpaceONE](https://github.com/spaceone-dev) on Docker. 

Manage your infrastructure with SpaceONE. It doesn't matter what your infrastructure is based on. SpaceONE supports AWS, GCP, Azure, IDC, ...etc.

![preview](https://helm.stargate.spaceone.dev/media/preview.png)

# ⭐️ Installation

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

# - configuration for secret service
#   role: secret manager (read/write)
AWS_ACCESS_KEY_ID=<Update YOUR AWS KEY ID>
AWS_SECRET_ACCESS_KEY=<Update YOUR AWS SECRET ACCESS KEY>
REGION_NAME=<Your Region for saving credential keys>

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
RUN_CONSUL = y
RUN_BACKEND = y
RUN_FRONTEND = y
RUN_SUPERVISOR = y
RUN_TESTER = y
```

Create AWS credentials at AWS console.
Update values for AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KET_ID, and REGION_NAME.

This credentials are used at secret service for saving SpaceONE credentials.


In the repository root directory, install SpaceONE.

```
$ make all
```

You can see the console page via http://console-client

## Initialize database

### 1. Create Root domain.

To run SpaceONE, 'root' domain must be initialized. This provides supervisor and repository services for other domains.

```
$ docker cp scenarios debug_identity_1:/root/
$ docker exec -ti debug_identity_1 /bin/bash
# In a debug_identity_1
$ pip install spaceone-tester
$ cd /root/root_domain
$ spaceone test
$ cd /root/register_plugins
$ spaceone test
```

### 2. Update DNS for web browser access.

To access specific domain, the URL is http://root

edit your hosts file for access.

In Linux PC or MacOS, edit /etc/hosts
In Windows PC, edit c:\windows\system32\drivers\etc\hosts

```
#
127.0.0.1 root
127.0.0.1 dev
```

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
