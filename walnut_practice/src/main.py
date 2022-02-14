from flask import Flask

from routes.recipe import recipe_bp

app = Flask(__name__)

app.register_blueprint(recipe_bp, url_prefix='/')

if __name__ == '__main__':
    app.debug = True
    app.run()