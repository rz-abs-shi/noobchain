from datetime import datetime
from crypto.utils import sha256
from crypto.utils import merkle_root


class Block:

    def __init__(self, previous_hash):

        self.previous_hash = previous_hash
        self.nonce = 0
        self.timestamp = datetime.now().timestamp()
        self.transactions = []
        self.hash = self.calculate_hash()

    def get_message(self):
        return self.previous_hash + str(self.nonce) + str(self.timestamp) + self.get_merkle_root()

    def calculate_hash(self):

        message = self.get_message()
        return sha256(message)

    def mine(self, difficulty=5):

        hash_prefix = '0' * difficulty

        while not self.hash.startswith(hash_prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()

    def get_merkle_root(self) -> str:
        transaction_ids = [transaction.transaction_id for transaction in self.transactions]
        return merkle_root(transaction_ids)

    def add_transaction(self, transaction, all_utxos, minimum_transaction) -> bool:
        if transaction is None:
            return False

        # process transaction and check if valid, unless block is genesis block then ignore.
        if self.previous_hash != "0":
            if not transaction.process_transaction(all_utxos, minimum_transaction):
                print("Transaction failed to process")
                return False

        self.transactions.append(transaction)
        return True

    def __str__(self):
        return self.hash

    def print(self):
        print("hash:", self.hash)
        print("transactions_count", len(self.transactions))
        print("merkle_root:", self.get_merkle_root())
        print("timestamp:", self.timestamp)
        print("nounce:", self.nonce)
        print("prev_hash:", self.previous_hash)
        print()
