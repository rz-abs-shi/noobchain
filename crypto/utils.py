from Crypto.PublicKey import RSA
import hashlib


def generate_rsa_keys(bits=2048):
    '''
    Generate an RSA keypair with an exponent of 65537 in PEM format
    param: bits The key length in bits
    Return private key and public key
    '''
    new_key = RSA.generate(bits, e=65537)
    public_key = new_key.publickey().exportKey("PEM")
    private_key = new_key.exportKey("PEM")
    return private_key, public_key


def sha256(message: str):

    message = message.encode()

    hash = hashlib.sha256()
    hash.update(message)

    return hash.hexdigest()