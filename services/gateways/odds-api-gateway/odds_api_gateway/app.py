from flask import Flask
import configparser
from api_consumer import OddsApiClient
from mappers import OddsApiSports, SPORTS_MAPPING
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

async def initial_load(api_client: OddsApiClient):

    logger.info("Starting to load sports")
    all_sports: dict = api_client.get_all_sports()
    
    # key: sport key from odds api
    # val: dict of other related values
    # e.g. sports_dict = {"americanfootball_ncaaf": {"group": "American Football", "active": True}}
    sports_dict = {}

    # initialise for sports we care about
    for sport in OddsApiSports:
        sports_dict[SPORTS_MAPPING[sport]] = {}
    
    for sports_full in all_sports:
        sports_key = sports_full["key"]
        if sports_key in sports_dict:
            sports_dict[sports_key]["group"] = sports_full["group"]
            sports_dict[sports_key]["active"] = sports_full["active"]
            sports_dict[sports_key]["has_outrights"] = sports_full["has_outrights"]
    

    logger.info("Sports info loaded, loading odds now")
    
    

