from blockchain import Block, BlockChain, Wallet, Transaction
from typing import Dict
from blockchain import TransactionOutput
from blockchain.genesis import get_genesis_transaction


if __name__ == '__main__':

    # a dictionary tracking unspent transaction outputs
    utxos = {}  # type: Dict[str, TransactionOutput]
    minimum_transaction = 0.1
    difficulty = 2

    blockchain = BlockChain(difficulty)

    wallet_one = Wallet(utxos)
    wallet_two = Wallet(utxos)

    wallet_coinbase = Wallet(utxos)

    # create genesis transaction, which sends 100 coins to wallet_one
    genesis_transaction = get_genesis_transaction(wallet_coinbase, wallet_one, 100, utxos)

    print("Creating and mining genesis block")
    genesis = Block("0")
    genesis.add_transaction(genesis_transaction, utxos, minimum_transaction)

    blockchain.append_block(genesis)

    # testing
    print("Wallet one balance: %d" % wallet_one.get_balance())

    print()
    print("Attemping to send funds (40) to Wallet two")
    block1 = Block(genesis.hash)
    block1.add_transaction(wallet_one.send_funds(wallet_two.public_key_as_str(), 40), utxos, minimum_transaction)
    blockchain.append_block(block1)
    print("Wallet one balance: %d" % wallet_one.get_balance())
    print("Wallet two balance: %d" % wallet_two.get_balance())

    print()
    print("Block 1")
    block1.print()

    print()
    print("Attempting to send more funds (1000) than it has")
    block2 = Block(block1.hash)
    block2.add_transaction(wallet_one.send_funds(wallet_two.public_key_as_str(), 1000), utxos, minimum_transaction)
    blockchain.append_block(block2)
    print("Wallet one balance: %d" % wallet_one.get_balance())
    print("Wallet two balance: %d" % wallet_two.get_balance())

    print()
    print("Block 2")
    block2.print()

    print("Wallet two is attempting to send funds (20) to wallet one")
    block3 = Block(block2.hash)
    block3.add_transaction(wallet_two.send_funds(wallet_one.public_key_as_str(), 20), utxos, minimum_transaction)
    blockchain.append_block(block3)
    print("Wallet one balance: %d" % wallet_one.get_balance())
    print("Wallet two balance: %d" % wallet_two.get_balance())

    print()
    print("Block 3")
    block3.print()

    print("is chain valid?", blockchain.check_valid(genesis_transaction))
