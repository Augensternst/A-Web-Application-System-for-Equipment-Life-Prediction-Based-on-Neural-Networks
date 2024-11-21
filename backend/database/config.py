CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",  # 数据库类型
            "credentials": {
                "host": "111.173.119.228",
                "port": "14082",
                "user": "root",
                "password": "18937082731",
                "database": "testdb"
            },
        },
    },
    "apps": {
        "models": {
            "models": ["database.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}
