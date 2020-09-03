# 🚀 SpaceONE Docker-Compose Installer

> a [SpaceONE](https://github.com/spaceone-dev) docker-compose to deploy [SpaceONE](https://github.com/spaceone-dev) on Docker. 

Manage your infrastructure with SpaceONE. It doesn't matter what your infrastructure is based on. SpaceONE supports AWS, GCP, Azure, IDC, ...etc.

![preview](https://helm.stargate.spaceone.dev/media/preview.png)

# ⭐️ Installation

This installation is for developer only.

### Requirements

* `docker`
* `docker-compose` 

### Deployment Architecture
![Deployment](https://raw.githubusercontent.com/spaceone-dev/spaceone-dockercompose/master/docs/docker-compose.png)

### Commands

```bash
mkdir spaceone
cd spaceone
git clone https://github.com/spaceone-dev/spaceone-dockercompose.git
cd spaceone-dockercompose
```

Base on your deploy environment,
You should update environment variables at build-data/environment/linux.mk.
For Mac User, edit mac.mk.
Especially **HOST_ADDR** and **HOST_FQDN** are important. This value is configured at supervisor micro-service.

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
#HOST_ADDR=$(shell ipconfig getifaddr en0)
# Linux
HOST_ADDR=$(shell curl http://169.254.169.254/latest/meta-data/public-ipv4)
HOST_FQDN=$(shell curl http://169.254.169.254/latest/meta-data/public-hostname)


############################
# Service List
############################
BACKEND = identity secret repository inventory inventory-scheduler inventory-worker plugin statistics monitoring
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
RUN_NGINX = y
```

In the repository root directory, install SpaceONE.

```bash
# For AWS EC2 linux user
$ make all ENV=linux

# For Mac User,
$ make all ENV=mac
```


### 1. Open web browser access.

You can see the console page via 

- https://domain name
- http://domain name:8280

NGINX includes self-signed certificate. So you have to accept self-signed certificate warning.

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
