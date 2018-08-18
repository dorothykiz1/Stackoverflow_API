class Config:
    DEBUG = False
    SECRET = "DEE1"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}

