from crypto.utils import generate_rsa_keys


class Wallet:

    def __init__(self):
        self.public_key = None
        self.private_key = None

        self.generate_key_pair()

    def generate_key_pair(self):
        self.private_key, self.public_key = generate_rsa_keys()
