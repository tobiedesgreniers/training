from flask import Flask

# local import
from instance.config import app_config
from routes.recipe import recipe_bp

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    app.register_blueprint(recipe_bp, url_prefix='/')

    return app