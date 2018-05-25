from crypto.utils import sha256


class Transaction:

    sequence = 0  # number of transactions created

    def __init__(self, from_pub_key: bytes, to_pub_key: bytes, value: float, ):
        self.sender = from_pub_key
        self.recipient = to_pub_key
        self.value = value
        self.transaction_id = None

    def calculate_hash(self):
        # increase the sequence to avoid 2 identical transactions having the same hash
        Transaction.sequence += 1

        message = self.sender.decode() + self.recipient.decode() + str(self.value) + str(Transaction.sequence)

        return sha256(message)
