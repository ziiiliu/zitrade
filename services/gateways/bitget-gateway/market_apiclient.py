import requests
from datetime import datetime

class APIClient:
    def __init__(self, base_url):
        """
        Initializes the APIClient with a base URL for the API.

        Parameters:
        - base_url (str): The base URL for the API endpoints.
        """
        self.base_url = base_url

    def get_candlestick_data(self, symbol, granularity, start_time=None, end_time=None):
        """
        Fetches candlestick data from the API.

        Parameters:
        - symbol (str): Trading pair (e.g., "BTCUSDT").
        - granularity (str): Chart time interval (e.g., "1min", "1h", "1day").
        - start_time (int, optional): Unix millisecond timestamp to get data after this time.
        - end_time (int, optional): Unix millisecond timestamp to get data before this time.
        - limit (int, optional): Number of data points to fetch (default 100, max 1000).

        Returns:
        - dict: The JSON response containing the candlestick data.
        """
        endpoint = "/api/v2/spot/market/candles"
        params = {
            "symbol": symbol,
            "granularity": granularity,
        }
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time

        return self._send_request("GET", endpoint, params)

    def _send_request(self, method, endpoint, params=None):
        """
        Sends a HTTP request to the specified API endpoint.

        Parameters:
        - method (str): HTTP method (e.g., "GET", "POST").
        - endpoint (str): API endpoint path.
        - params (dict, optional): Parameters to include in the request.

        Returns:
        - dict: The JSON response from the API.
        """
        url = self.base_url + endpoint
        response = requests.request(method, url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

# Example usage:
if __name__ == "__main__":
    client = APIClient("https://api.bitget.com")

    symbol = "BTCUSDT"
    granularity = "1min"
    start_time = int(datetime.strptime("2023-04-01 00:00:00", "%Y-%m-%d %H:%M:%S").timestamp() * 1000)
    end_time = int(datetime.strptime("2023-04-02 00:00:00", "%Y-%m-%d %H:%M:%S").timestamp() * 1000)

    data = client.get_candlestick_data(symbol, granularity, start_time, end_time, limit)
    print(data)