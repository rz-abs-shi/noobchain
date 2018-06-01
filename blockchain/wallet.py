from typing import Dict

from blockchain import TransactionOutput, Transaction, TransactionInput
from crypto.rsa import new_keys
from Crypto.PublicKey.RSA import RsaKey


class Wallet:

    def __init__(self, all_utxos: Dict[str, TransactionOutput]):
        self.public_key = None  # type: RsaKey
        self.private_key = None  # type: RsaKey

        self.utxos = {}  # type: Dict[str, TransactionOutput]
        self.all_utxos = all_utxos

        self.generate_key_pair()

    def generate_key_pair(self):
        self.public_key, self.private_key = new_keys(2048)

    def public_key_as_str(self):
        return self.public_key.export_key().decode()

    def private_key_as_str(self):
        return self.private_key.export_key().decode()

    def print(self):
        print("Public key: " + self.public_key_as_str())
        print("Private key: " + self.private_key_as_str())

    def get_balance(self):
        self.update_utxos()

        amount = 0

        for utxo in self.utxos.values():
            amount += utxo.value

        return amount

    def update_utxos(self):
        self.utxos = {}
        my_public_key = self.public_key_as_str()

        for output_id, utxo in self.all_utxos.items():
            if utxo.is_mine(my_public_key):
                self.utxos[output_id] = utxo

    def send_funds(self, recipient_public_key_str: str, value: float) -> Transaction:
        self.update_utxos()

        if self.get_balance() < value:
            print("Not enough balance, transaction discarded")
            return

        if value <= 0:
            print("Value should be positive, transaction discarded")
            return

        inputs = []
        total = 0
        for transaction_id, utxo in self.utxos.items():
            total += utxo.value
            inp = TransactionInput(transaction_id)
            inputs.append(inp)

            if total >= value:
                break

        transaction = Transaction(self.public_key_as_str(), recipient_public_key_str, value, inputs)
        transaction.generate_signature(self.private_key)

        for inp in inputs:
            del self.utxos[inp.transaction_output_id]

        return transaction
