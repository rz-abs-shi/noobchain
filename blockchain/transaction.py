from crypto.utils import sha256
from crypto.rsa import sign, verify, import_key
from typing import List
from blockchain import TransactionOutput, TransactionInput


class Transaction:

    sequence = 0  # number of transactions created

    def __init__(self, from_pub_key_str: str, to_pub_key_str: str, value: float, inputs: list):
        self.sender = from_pub_key_str
        self.recipient = to_pub_key_str
        self.value = value
        self.transaction_id = None
        self.signature = None

        # transaction inputs for creating this transaction
        self.inputs = inputs  # type: List[TransactionInput]

        # transaction outputs created from this transaction
        self.outputs = None  # type: List[TransactionOutput]

    def calculate_hash(self):
        # increase the sequence to avoid 2 identical transactions having the same hash
        Transaction.sequence += 1

        message = self.sender + self.recipient + str(self.value) + str(Transaction.sequence)

        return sha256(message)

    def generate_signature(self, sender_private_key):
        message = self.sender + self.recipient + str(self.value)
        self.signature = sign(message.encode(), sender_private_key)

    def verify_signature(self):
        if not self.signature:
            return False

        message = self.sender + self.recipient + str(self.value)
        sender_public_key = import_key(self.sender)
        return verify(message.encode(), self.signature, sender_public_key)

    def get_outputs_value(self):

        amount = 0

        for output in self.outputs:
            amount += output.value

        return amount

    def get_inputs_value(self):

        amount = 0

        for input in self.inputs:
            if input.utxo:
                amount += input.utxo.value

        return amount
