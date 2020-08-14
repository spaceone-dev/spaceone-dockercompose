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
#AWS_ACCESS_KEY_ID=
#AWS_SECRET_ACCESS_KEY=
#REGION_NAME=

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
