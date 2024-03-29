import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET') # secret = 4kyPji7TEnSlDkYZU6HE


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
