from decimal import Decimal
from web3 import Web3
import json


class Parser:
    def __init__(self, chain, rawTxs, presale, token):
        self.rawTxs = rawTxs
        self.presale = presale
        self.token = token
        self.chain = chain

    def parse_txs(self):
        if self.token == "NATIVE":
            return self.parse_native_txs()
        else:
            return self.parse_token_txs()

    def parse_native_txs(self):
        value = 0
        for key in self.rawTxs:
            if key["to"] == "":
                continue
            if (
                Web3.toChecksumAddress(key["to"])
                == Web3.toChecksumAddress(self.presale)
                and int(key["value"]) > 0
            ):
                value += int(key["value"])

        return json.dumps(
            {
                "network": self.chain,
                "presale": self.presale,
                "token": self.token,
                "amount": float(Decimal(value) / (Decimal(10) ** 18)),
            }
        )

    def parse_token_txs(self):
        value = 0
        decimal = int(self.rawTxs[0]["tokenDecimal"])
        for key in self.rawTxs:
            if (
                Web3.toChecksumAddress(key["to"])
                == Web3.toChecksumAddress(self.presale)
                and int(key["value"]) > 0
            ):
                value += int(key["value"])

        return json.dumps(
            {
                "network": self.chain,
                "presale": self.presale,
                "token": self.token,
                "symbol": self.rawTxs[0]["tokenSymbol"],
                "amount": float(Decimal(value) / (Decimal(10) ** decimal)),
            }
        )
