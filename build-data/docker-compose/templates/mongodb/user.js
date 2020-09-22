db.auth('admin','password')
db = db.getSiblingDB('identity')
db.createUser(
    {
        user: "identity",
        pwd: "identity_password",
        roles: [ {role: "readWrite", db: "identity" } ]
    }
);
db.auth('admin','password')
db = db.getSiblingDB('inventory')
db.createUser(
    {
        user: "inventory",
        pwd: "inventory_password",
        roles: [ {role: "readWrite", db: "inventory" } ]
    }
);
db.auth('admin','password')
db = db.getSiblingDB('repository')
db.createUser(
    {
        user: "repository",
        pwd: "repository_password",
        roles: [ {role: "readWrite", db: "repository" } ]
    }
);
db.auth('admin','password')
db = db.getSiblingDB('plugin')
db.createUser(
    {
        user: "plugin",
        pwd: "plugin_password",
        roles: [ {role: "readWrite", db: "plugin" } ]
    }
);
db.auth('admin','password')
db = db.getSiblingDB('secret')
db.createUser(
    {
        user: "secret",
        pwd: "secret_password",
        roles: [ {role: "readWrite", db: "secret" } ]
    }
);
db.auth('admin','password')
db = db.getSiblingDB('monitoring')
db.createUser(
    {
        user: "monitoring",
        pwd: "monitoring_password",
        roles: [ {role: "readWrite", db: "monitoring" } ]
    }
);
db.auth('admin','password')
db = db.getSiblingDB('statistics')
db.createUser(
    {
        user: "statistics",
        pwd: "statistics_password",
        roles: [ {role: "readWrite", db: "statistics" } ]
    }
);
db.auth('admin','password')
db = db.getSiblingDB('power_scheduler')
db.createUser(
    {
        user: "power_scheduler",
        pwd: "power_scheduler_password",
        roles: [ {role: "readWrite", db: "power_scheduler" } ]
    }
);
db.auth('admin','password')
db = db.getSiblingDB('marketplace')
db.createUser(
    {
        user: "repository",
        pwd: "repository_password",
        roles: [ {role: "readWrite", db: "marketplace" } ]
    }
);
