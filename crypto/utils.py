from Crypto.PublicKey import RSA
import hashlib
from typing import List
import math


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


def merkle_root(nodes: List[str]):
    if len(nodes) == 0:
        return ""

    elif len(nodes) == 1:
        return sha256(nodes[0])

    layer = nodes

    while len(layer) > 1:
        if len(layer) % 2 == 1:
            layer.append("")

        new_layer = [None] * (len(layer) // 2)

        for i in range(len(new_layer)):
            new_layer[i] = sha256(layer[2 * i] + layer[2 * i + 1])

        layer = new_layer

    return layer[0]
