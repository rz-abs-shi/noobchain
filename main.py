from blockchain import Block, BlockChain


if __name__ == '__main__':

    blockchain = BlockChain()

    blockchain.append_new_block("Start block")
    blockchain.append_new_block("Next block")
    blockchain.append_new_block("Third block")

    blockchain.print()

    print("Blockchain is valid: " + str(blockchain.check_valid()))