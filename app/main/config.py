import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

SWAGGER_VERSION = 0.1


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'test secretkey')
    DEBUG = False


# 외부 API와 연동하기 위해서 사용되는 Access키나 Secret Key의 경우 보안상 코드상에 저장하면 안되기 때문에
# 환경변수화 해서 가져옴


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


# uncomment the line below to use postgres
# SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY

SWAGGER_CONFIG = {
    'headers': [],  # ResponseHeader
    'specs': [
        {
            'endpoint': 'apispec',
            'route': '/apispec.json',
            'rule_filter': lambda rule: str(rule).startswith('/'),
            'model_filter': lambda tag: True,  # all in
        }
    ],
    'hide_top_bar': True,
    'static_url_path': '/flasgger_static',
    # 'template_folder': '/swagger_ui/templates',
    # 'static_folder': '/swagger_ui/static',
    'swagger_ui': True,
    'specs_route': '/api-docs/',
    'version': SWAGGER_VERSION,
    'title': 'Yeohanglog API Document',
    'description': 'API Document for Server',
    'uiversion': 3,
    # 'basePath': '/api',
    'termsOfService': '',
    'schemes': [
        'http',
        'https'
    ]
}
