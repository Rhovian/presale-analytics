# address = "0xd82477E8e75f18D210770574F57f31D57FBfC50f"
import argparse
from queries import QueryHandler


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-c",
        "--chain",
        type=str,
        required=True,
        help="Choose a supported chain: ethereum, bsc, polygon",
    )

    parser.add_argument(
        "-p",
        "--presale",
        type=str,
        required=True,
        help="A target contract address (presale) is required",
    )

    parser.add_argument(
        "-t",
        "--token",
        type=str,
        required=True,
        help="A target token address, or NATIVE, is required",
    )

    args = parser.parse_args()

    query_handler = QueryHandler(args.chain, args.presale, args.token)

    transactions = query_handler.run()
    print("Transactions found: {}".format(len(transactions["result"])))


if __name__ == "__main__":
    main()
