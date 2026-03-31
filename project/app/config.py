#CLASS EXAMPLE FOR CONFIGURATION THE PROD BASE ON THE DEV CONFIG

class DevelopmentConfig:
    DEBUG = True
    DATABASE_URL = "postgresql://user:pass@localhost/dev_db"
    SECRET_KEY = "dev_key"


class ProductionConfig:
    DEBUG = False
    DATABASE_URL = "postgresql://user:pass@localhost/prod_db"
    SECRET_KEY = "prod_key"