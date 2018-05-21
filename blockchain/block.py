from datetime import datetime
import hashlib
import base64


class Block:

    def __init__(self, data, previous_hash):

        self.data = data
        self.previous_hash = previous_hash
        self.nounce = 0
        self.timestamp = datetime.now().timestamp()
        self.hash = self.calculate_hash()

    def get_message(self):
        return self.data + self.previous_hash + str(self.nounce) + str(self.timestamp)

    def calculate_hash(self):

        message = self.get_message().encode()

        hash = hashlib.sha256()
        hash.update(message)

        digest = hash.digest()

        return base64.b64encode(digest)

    def __str__(self):
        return self.hash
