import asyncio
from aiohttp import ClientSession
import configparser
import requests
import json

CONFIG_SECTION = "odds_api"
"""
Odds API doc page: https://the-odds-api.com/liveapi/guides/v4/
Odds API swagger page: https://app.swaggerhub.com/apis-docs/the-odds-api/odds-api/4 
"""

class OddsApiClient:
    def __init__(self, cfg):
        self.host = cfg
        self.host = cfg.get(CONFIG_SECTION, "HOST")
        self.api_key = cfg.get(CONFIG_SECTION, "API_KEY")

    def get_all_sports(self) -> dict:
        resp = requests.get(url=f"{self.host}/v4/sports/?apiKey={self.api_key}")
        status = resp.status_code
        resp_json = resp.json()
        print(resp_json)
        return resp_json
    
    def get_odds(self, sport, regions, markets) -> dict:
        """
        TODO: include potentially important optional parameters. E.g. eventIds, bookmakers
        """
        resp = requests.get(url=f"{self.host}/v4/sports/{sport}/odds/?apiKey={self.api_key}&regions={regions}&markets={markets}")
        resp_json = resp.json()
        print(resp_json)
        return resp_json

    def get_scores(self, sport, days_from, date_format) -> dict:
        resp = requests.get(url=f"{self.host}/v4/sports/{sport}/scores/?apiKey={self.api_key}&daysFrom={days_from}&dateFormat={date_format}")
        resp_json = resp.json()
        print(resp_json)
        return resp_json
    
    def get_historical_odds(self, sport, regions, markets, date):
        resp = requests.get(url=f"{self.host}/v4/sports/{sport}/odds-history/?apiKey={self.api_key}&regions={regions}&markets={markets}&date={date}")
        resp_json = resp.json()
        print(resp_json)
        return resp_json
    
    def get_event_odds(self, sport, regions, markets, event_id, date_format, odds_format):
        resp = requests.get(url=f"{self.host}/v4/sports/{sport}/events/{event_id}/?apiKey={self.api_key}&regions={regions}&markets={markets}&dateFormat={date_format}&oddsFormat={odds_format}")
        resp_json = resp.json()
        print(resp_json)
        return resp_json

if __name__ == "__main__":

    cfg = configparser.ConfigParser()
    cfg.read("./api_config.cfg")
    client = OddsApiClient(cfg)
    res = client.get_historical_odds("baseball_mlb", "uk", "h2h", "2023-07-30T12:00:00Z")

    # with open("tests/sample_historical_odds.json", "w") as file:
    #     json.dump(res, file)