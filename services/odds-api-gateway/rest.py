from aiohttp import web
from api_consumer import OddsApiClient
import configparser

routes = web.RouteTableDef()

class Handler:

    def __init__(self, cfg):
        self.api_consumer = OddsApiClient(cfg)

    async def get_market_odds(self, request):
        market_id = request.match_info["market_id"]
        self.api_consumer.get_odds()

if __name__ == "__main__":

    cfg = configparser.ConfigParser()
    cfg.read("./api_config.cfg")
    handler = Handler(cfg)

