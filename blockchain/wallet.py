from crypto.rsa import new_keys


class Wallet:

    def __init__(self):
        self.public_key = None
        self.private_key = None

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
