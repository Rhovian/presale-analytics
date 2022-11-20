from etherscan.accounts import Account
import os
from dotenv import load_dotenv, find_dotenv
import requests

load_dotenv(find_dotenv())

ETHERSCAN_KEY = os.environ.get("ETHERSCAN_KEY")


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
        if res.status_code == 200:
            return res.json()

    def build_query_native(self):
        if self.chain == "ethereum":
            self.query = (
                "https://api.etherscan.io/api?module=account&action=txlist&address="
                + self.presale
                + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey="
                + ETHERSCAN_KEY
            )

    def build_query_token(self):
        if self.chain == "ethereum":
            self.query = (
                "https://api.etherscan.io/api?module=account&action=tokentx&contractAddress="
                + self.token
                + "&address="
                + self.presale
                + "&page=1&offset=100&startblock=0&endblock=27025780&sort=asc&apikey="
                + ETHERSCAN_KEY
            )
