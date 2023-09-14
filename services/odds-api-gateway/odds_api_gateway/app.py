from flask import Flask
import configparser
from api_consumer import OddsApiClient
from common_lib.worker import PeriodicWorker
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_PULL_PERIOD_SECS = 20

def create_rest_app(api_client: OddsApiClient) -> Flask:

    app = Flask(__name__)
    from rest import blueprint
    app.register_blueprint(blueprint)
    app.config["api_client"] = api_client
    return app

async def setup():
    logger.info("reading config file")
    cfg = configparser.ConfigParser()
    cfg.read("./api_config.cfg")
    api_client = OddsApiClient(cfg)

    loop = asyncio.get_event_loop()
    print(loop)

    worker = PeriodicWorker(api_client.get_all_sports, API_PULL_PERIOD_SECS)
    
    # Create a task to run the worker concurrently
    worker_task = loop.create_task(worker.start())
    # await worker_task
    logger.info("Main program continues to run in parallel...")
    return api_client, worker_task