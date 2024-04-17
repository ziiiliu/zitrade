from odds_api_gateway.api_consumer import OddsApiClient
import configparser

class TestConsumerClient:
    def setup_client(self) -> OddsApiClient:
        cfg = configparser.ConfigParser()
        cfg.read("./api_config.cfg")
        return OddsApiClient(cfg)

    def test_get_all_sports(self):
        client = self.setup_client()
        all_sports = client.get_all_sports()
        print(f"All sports json: {all_sports}")
        assert all_sports is not None

    def test_get_odds(self):
        pass

    def test_get_scores(self):
        pass

    def test_get_historical_odds(self):
        pass

    def test_get_event_odds(self):
        pass