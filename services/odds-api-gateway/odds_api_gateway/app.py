from flask import Flask
import configparser
from api_consumer import OddsApiClient
from lib.worker import PeriodicWorker
import asyncio

API_PULL_PERIOD_SECS = 20

def create_rest_app(api_client: OddsApiClient) -> Flask:

    app = Flask(__name__)
    from rest import blueprint
    app.register_blueprint(blueprint)
    app.config["api_client"] = api_client
    return app

def setup():
    cfg = configparser.ConfigParser()
    cfg.read("../api_config.cfg")
    api_client = OddsApiClient(cfg)

    worker = PeriodicWorker(api_client.get_all_sports, API_PULL_PERIOD_SECS)
    
    # Create a task to run the worker concurrently
    _worker_task = asyncio.create_task(worker.start())

    print("Main program continues to run in parallel...")
    return api_client