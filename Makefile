export WS_ROOT=$(shell pwd)
export ENV?=debug
export BR=$(WS_ROOT)/build-root
export TARGET?=docker-compose

#export CACHE=${date +%s}
#export CACHE=PUT_RANDOM_STRING

define banner
	@echo "========================================================================"
	@echo " $(1)"
	@echo "========================================================================"
	@echo " "
endef

.PHONY: config
config:
	@echo "======================================================================="
	@echo "Environment: $(ENV)"
	@echo "Target     : $(TARGET)"
	@echo "build dir  : $(BR)"
	@echo "======================================================================="
	mkdir -p $(BR)
	rm -rf $(BR)/$(ENV)
	cp -r build-data/$(TARGET) $(BR)/$(ENV)
	cp -r build-data/scenarios $(BR)/$(ENV)/
	cp build-data/environments/$(ENV).mk $(BR)/$(ENV)/build.mk 
	make -C $(BR)/$(ENV) config

.PHONY: supervisor
supervisor: config
	$(call banner, "Install supervisor at $${BR}")
	make -C $(BR)/$(ENV) debug

.PHONY: backend
backend:
	make -C $(BR)/$(ENV) backend

.PHONY: frontend
frontend:
	make -C $(BR)/$(ENV) frontend

.PHONY: tester
tester:
	make -C $(BR)/$(ENV) tester


.PHONY: debug
debug: 
	make -C $(BR)/$(ENV) debug

.PHONY: api
api:
	cd api; make all

.PHONY: clean
clean:
	make -C $(BR)/$(ENV) clean
	rm -rf $(BR)/$(ENV)

#all: config backend frontend tester debug
all: config debug

help:
	@echo "Make Targets:"
	@echo " api                                          - build protobuf API"
	@echo " config   ENV=<Environment Name>              - config based on environment file(build-data/environments/<environment name>.mk)"
	@echo " backend  ENV=<Environment Name>              - build backend Docker images"
	@echo " frontend ENV=<Environment Name>              - build frontend Docker images"
	@echo " debug    ENV=<Environment Name>              - run environment"
	@echo " tester   ENV=<Environment Name>              - initialize scenario files"
	@echo " clean    ENV=<Environment Name>              - clean up all information"
	@echo " all      ENV=<Environment Name>              - run all-in-one (API -> config -> backend -> frontend -> debug)"
