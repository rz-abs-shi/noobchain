from blockchain import TransactionOutput


class TransactionInput:
    def __init__(self, transaction_output_id: str):
        self.transaction_output_id = transaction_output_id
        self.utxo = None  # type: TransactionOutput

