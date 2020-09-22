############################
# Docker Image Registry
#############################
#IMAGE_REGISTRY=spaceone
IMAGE_REGISTRY=pyengine
VERSION=latest

############################
# Update Your environment
# - supervisor (private ip address of this machine)
# MacOS
#HOST_ADDR=$(shell ipconfig getifaddr en0)
# Linux
#HOST_ADDR=$(shell hostname -i)
# AWS EC2
HOST_ADDR=$(shell curl http://169.254.169.254/latest/meta-data/public-ipv4)
HOST_FQDN=$(shell curl http://169.254.169.254/latest/meta-data/public-hostname)

# - configuration for secret service
#   role: secret manager (read/write)
#AWS_ACCESS_KEY_ID=
#AWS_SECRET_ACCESS_KEY=
#REGION_NAME=

############################
# Service List
############################
BACKEND = identity secret repository inventory inventory-scheduler inventory-worker plugin statistics monitoring power_scheduler
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
