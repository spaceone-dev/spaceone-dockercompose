-include build.mk

.PHONY: config backend frontend tester debug clean

config:

ifeq (${RUN_MONGODB},y)
	cat $(BR)/$(ENV)/templates/mongodb/docker-compose.yml >> $(BR)/$(ENV)/docker-compose.yml
endif

ifeq (${RUN_REDIS},y)
	cat $(BR)/$(ENV)/templates/redis/docker-compose.yml >> $(BR)/$(ENV)/docker-compose.yml
endif

ifeq (${RUN_VAULT},y)
	cat $(BR)/$(ENV)/templates/vault/docker-compose.yml >> $(BR)/$(ENV)/docker-compose.yml
	cp $(BR)/$(ENV)/templates/vault/vault.json $(BR)/$(ENV)/data/vault/config/vault.json
endif

ifeq (${RUN_CONSUL},y)
	cat $(BR)/$(ENV)/templates/consul/docker-compose.yml >> $(BR)/$(ENV)/docker-compose.yml
endif

ifeq (${RUN_BACKEND},y)
	@for t in $(BACKEND); do \
		cat $(BR)/$(ENV)/templates/$$t/docker-compose.yml >> $(BR)/$(ENV)/docker-compose.yml ; \
		cp $(BR)/$(ENV)/templates/$$t/$$t.yml $(BR)/$(ENV)/conf/$$t.yml ; \
	done
endif

ifeq (${RUN_FRONTEND},y)
	@for t in $(FRONTEND); do \
		cat $(BR)/$(ENV)/templates/$$t/docker-compose.yml >> $(BR)/$(ENV)/docker-compose.yml ; \
		cp $(BR)/$(ENV)/templates/$$t/production.json $(BR)/$(ENV)/conf/production.json.$$t ; \
	done
endif

ifeq (${RUN_SUPERVISOR},y)
	@for t in $(SUPERVISOR); do \
		cat $(BR)/$(ENV)/templates/$$t/docker-compose.yml >> $(BR)/$(ENV)/docker-compose.yml ; \
		cp $(BR)/$(ENV)/templates/$$t/$$t.yml $(BR)/$(ENV)/conf/$$t.yml ; \
	done
endif

ifeq (${RUN_TESTER},y)
	@for t in $(TESTER); do \
		cat $(BR)/$(ENV)/templates/$$t/docker-compose.yml >> $(BR)/$(ENV)/docker-compose.yml ; \
	done

endif

	@echo "Update Configuration variables ...."
	@echo "Build Root: $(BR)"
	@echo "ENV: $(ENV)"
	@echo "-------------"
	sed -i -e 's/IMAGE_REGISTRY/$(IMAGE_REGISTRY)/g' docker-compose.yml
	sed -i -e 's/SUPERVISOR_HOSTNAME/$(SUPERVISOR_HOSTNAME)/g' conf/supervisor.yml
	sed -i -e 's/AWS_ACCESS_KEY_ID/$(AWS_ACCESS_KEY_ID)/g' conf/secret.yml
	sed -i -e 's/AWS_SECRET_ACCESS_KEY/$(AWS_SECRET_ACCESS_KEY)/g' conf/secret.yml
	sed -i -e 's/REGION_NAME/$(REGION_NAME)/g' conf/secret.yml

backend:
	@for t in $(BACKEND); do \
		docker build -t test/$$t $(WS_ROOT)/$$t/ --build-arg CACHEBUST=$(CACHE) ; \
	done
	$(call banner, "Created Docker Images: tests: $(BACKEND)")

frontend:
	@for t in $(FRONTEND); do \
		docker build -t test/$$t $(WS_ROOT)/$$t/ --build-arg CACHEBUST=$(CACHE) ; \
	done
	$(call banner, "Created Docker Images: tests: $(FRONTEND)")

tester:
	@for t in $(TESTER); do \
		docker build -t test/$$t $(WS_ROOT)/$$t/ --build-arg CACHEBUST=$(date +%s) ; \
	done
	$(call banner, "Created Docker Images: tests: $(TESTER)")

debug:
	docker-compose up

clean:
	docker-compose down
	docker-compose rm -v -f
