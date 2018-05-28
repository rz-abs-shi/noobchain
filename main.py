from blockchain import Block, BlockChain, Wallet, Transaction
from blockchain import DIFFICULTY
from typing import Dict
from blockchain import TransactionOutput

if __name__ == '__main__':

    wallet1 = Wallet()
    wallet2 = Wallet()
    # a dictionary tracking unspent transaction outputs
    utxos = {}  # type: Dict[str, TransactionOutput]

    print("Wallet 1")
    wallet1.print()

    transaction = Transaction(wallet1.public_key_as_str(), wallet2.public_key_as_str(), 5)
    transaction.generate_signature(wallet1.private_key)

    print("transaction verified?")
    print(transaction.verify_signature())
