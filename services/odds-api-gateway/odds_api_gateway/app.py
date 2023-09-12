from flask import Flask
import configparser
from api_consumer import OddsApiClient

def create_app():
    cfg = configparser.ConfigParser()
    cfg.read("../api_config.cfg")
    api_client = OddsApiClient(cfg)

    app = Flask(__name__)
    from rest import blueprint
    app.register_blueprint(blueprint)
    app.config["api_client"] = api_client
    return app
