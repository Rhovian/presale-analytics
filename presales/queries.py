import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

ETHERSCAN_KEY = os.environ.get("ETHERSCAN_KEY")
POLYGON_KEY = os.environ.get("POLYGON_KEY")
BSC_KEY = os.environ.get("BSC_KEY")

ETH_URL_BASE = "https://api.etherscan.io/api?module=account"
POLYGON_URL_BASE = "https://api.polygonscan.com/api?module=account"
BSC_URL_BASE = "https://api.bscscan.com/api?module=account"


class QueryHandler:
    def __init__(self, chain, presale, token):
        self.chain = chain
        self.presale = presale
        self.token = token
        self.query = ""

    def run(self):
        if self.token == "NATIVE":
            self.build_query_native()
        else:
            self.build_query_token()

        res = requests.get(self.query)
        res = res.json()

        if res["status"] == "1":
            return res
        else:
            raise Exception("Error in Query Module. Message: {}".format(res["result"]))

    def build_query_native(self):
        base = ETH_URL_BASE
        key = ETHERSCAN_KEY

        if self.chain == "polygon":
            base = POLYGON_URL_BASE
            key = POLYGON_KEY
        elif self.chain == "bsc":
            base = BSC_URL_BASE
            key = BSC_KEY

        self.query = (
            base
            + "&action=txlist&address="
            + self.presale
            + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey="
            + key
        )

    def build_query_token(self):
        base = ETH_URL_BASE
        key = ETHERSCAN_KEY

        if self.chain == "polygon":
            base = POLYGON_URL_BASE
            key = POLYGON_KEY
        elif self.chain == "bsc":
            base = BSC_URL_BASE
            key = BSC_KEY

        self.query = (
            base
            + "&action=tokentx&contractAddress="
            + self.token
            + "&address="
            + self.presale
            + "&page=1&offset=100&startblock=0&endblock=27025780&sort=asc&apikey="
            + key
        )
