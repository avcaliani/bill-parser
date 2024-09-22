from ofxparse import OfxParser
from ofxparse.ofxparse import Ofx


def _read(file_path: str) -> Ofx:
    with open(file_path, "r", encoding="ISO-8859-1") as ofx_file:
        return OfxParser.parse(ofx_file)


def get_transactions(file_path: str) -> dict:
    ofx_data, transactions = _read(file_path), []
    for tx in ofx_data.account.statement.transactions:
        transactions.append(
            {
                "tx_id": tx.id,
                "tx_type": tx.type,
                "tx_date": tx.date.strftime("%Y-%m-%d"),
                "tx_amount": float(tx.amount),
                "tx_description": tx.memo,
            }
        )
    return transactions
