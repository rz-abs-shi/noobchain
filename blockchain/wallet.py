from typing import Dict

from blockchain import TransactionOutput
from crypto.rsa import new_keys


class Wallet:

    def __init__(self):
        self.public_key = None
        self.private_key = None
        self.utxos = {}  # type: Dict[str, TransactionOutput]

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
        amount = 0

        for utxo in self.utxos.values():
            amount += utxo.value

        return amount

    def update_utxos(self, all_utxos: Dict[str, TransactionOutput]):
        self.utxos = {}
        my_public_key = self.public_key_as_str()

        for output_id, utxo in all_utxos.items():
            if utxo.is_mine(my_public_key):
                self.utxos[output_id] = utxo

    def send_funds(self):
        pass