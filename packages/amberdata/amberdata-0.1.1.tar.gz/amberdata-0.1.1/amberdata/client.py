from typing import Dict
import requests
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

from amberdata import queries, types


class Amberdata:
    """Amberdata API client.

    Contact hello@amberdata.io for API key information.
    """

    _url = "https://web3api.io/api/v2/"

    def __init__(self,  x_api_key: str) -> None:
        """Initializes Amberdata API client.

        Args:
            x_api_key (str): API key
        """
        self.headers = {
            "x-api-key": f"{x_api_key}",
            "accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
            "x-amberdata-blockchain-id": "ethereum-mainnet"
        }

    def blockchain_address_logs(
        self, address, topic, page = 0, size=1
    ) -> Dict:
        """
        Returns the current orderbook of options

        Args:
            symbol: BTC / ETH / SOL (deribit) / BCH (bitcom)
            exchange: deribit / bitcom / okex / ledgerx

        Returns:
            {
            "ts": "1637677441586",
            "instrumentName": "BTC-24NOV21-59000-C",
            "strike": 59000,
            "expiration": "1637712000000",
            "bidIv": 59.4,
            "markIv": 66.33,
            "askIv": 71.68,
            "delta": 0.10811
            }

        """
        full_url = self._url + f"addresses/{address}/logs?topic={topic}&page={page}&size={size}"    
        response = requests.get(url=full_url, headers=self.headers)
        data_out = response.json()
        if response.status_code >= 200 and response.status_code <= 299:     # OK
            return data_out
        raise Exception(data_out["message"]) 

       

   