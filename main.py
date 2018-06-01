from blockchain import Block, BlockChain, Wallet, Transaction
from typing import Dict
from blockchain import TransactionOutput
from blockchain.genesis import get_genesis_transaction


if __name__ == '__main__':

    # a dictionary tracking unspent transaction outputs
    utxos = {}  # type: Dict[str, TransactionOutput]
    minimum_transaction = 0.1
    difficulty = 3

    blockchain = BlockChain(difficulty)

    wallet_one = Wallet(utxos)
    wallet_two = Wallet(utxos)

    wallet_coinbase = Wallet(utxos)

    # create genesis transaction, which sends 100 coins to wallet_one
    genesis_transaction = get_genesis_transaction(wallet_coinbase, wallet_one, 100)

    print("Creating and mining genesis block")
    genesis = Block("0")
    genesis.add_transaction(genesis_transaction, utxos, minimum_transaction)

    blockchain.append_block(genesis)
