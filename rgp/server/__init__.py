from flask import Flask
import os
from flask_cors import CORS, cross_origin

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./pages")
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../static")

def create_app():
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    with app.app_context():
        from . import route
    return app

def run_app():
    app = create_app()
    port = int(os.environ.get("PORT", 3000))
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["DEBUG"] = True
    app.run(host="0.0.0.0", port=port)
