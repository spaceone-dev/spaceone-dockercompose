############################
# Docker Image Registry
#############################
IMAGE_REGISTRY=spaceone
VERSION=1.3.2

############################
# Update Your environment
# - supervisor (private ip address of this machine)
# MacOS
HOST_ADDR=$(shell ipconfig getifaddr en0)
HOST_FQDN=localhost

############################
# Service List
############################
#BACKEND = identity secret repository inventory inventory-scheduler inventory-worker plugin statistics monitoring \
#	  power_scheduler power_scheduler-scheduler power_scheduler-worker
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
