from argparse import ArgumentParser, Namespace
from pandas import DataFrame
from bill_parser import ofx


def get_args() -> Namespace:
    parser = ArgumentParser(description="Bill Parser")
    parser.add_argument("file", type=str, help="OFX file path.")
    return parser.parse_args()


def bold(value: str) -> str:
    return f"\033[1m{value}\033[00m"


def green(value: str) -> str:
    return f"\033[1;32m{value}\033[00m"


if __name__ == "__main__":
    print(bold("Welcome to Bill Parser 👋"))
    args = get_args()
    ofx_path = args.file
    csv_path = ofx_path.replace("ofx", "csv")

    print(f"➜ reading file: {ofx_path}", end=" ")
    transactions = ofx.get_transactions(ofx_path)
    print(green("✔"))

    print(f"➜ transactions: {green(len(transactions))} 💸")

    print(f"➜ writing the new file...", end=" ")
    DataFrame(transactions).to_csv(csv_path, index=False)
    print(green("✔"))

    print(bold("\nJOB DONE 🍻"))
    print(f"Check the result in the {bold(csv_path)} file")
