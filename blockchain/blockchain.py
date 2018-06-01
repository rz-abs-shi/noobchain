from blockchain import Block, Transaction


class BlockChain:

    def __init__(self, difficulty):
        self.blocks = []
        self.difficulty = difficulty

    def append_block(self, block: Block, mine_block=True):
        if mine_block:
            block.mine(self.difficulty)
            print("Block mined: " + block.hash)

        self.blocks.append(block)

    def check_valid(self, genesis_transaction: Transaction):
        hash_prefix = "0" * self.difficulty

        temp_utxos = dict()  # a temperory dictionary of unspent transactions
        temp_utxos[genesis_transaction.outputs[0].id] = genesis_transaction.outputs[0]

        prev_hash = self.blocks[0].hash
        for block_ind in range(1, len(self.blocks)):
            print("Checking block %d" % block_ind)

            block = self.blocks[block_ind]

            # compare registered hash and calculated hash
            if block.calculate_hash() != block.hash:
                print("Invalid hash")
                return False

            # check registered previous hash with its real previous hash
            if block.previous_hash != prev_hash:
                print("Invalid previous hash")
                return False

            prev_hash = block.hash

            # check if hash is solved
            if not block.hash.startswith(hash_prefix):
                print("Hash is not solved")
                return False

            # loop through transactions
            i = 0
            for transaction in block.transactions:
                if not transaction.verify_signature():
                    print("Signature is invalid on transaction %d" % i)
                    return False

                if transaction.get_inputs_value() != transaction.get_outputs_value():
                    print("Input values are not equal with output values on transaction %d" % i)
                    return False

                for inp in transaction.inputs:
                    output = temp_utxos.get(inp.transaction_output_id)

                    if not output:
                        print("Missing transaction input reference on transaction %d" % i)
                        return False

                    if output.value != inp.utxo.value:
                        print("Invalid transaction input value for transaction %d" % i)
                        return False

                    del temp_utxos[output.id]

                for output in transaction.outputs:
                    temp_utxos[output.id] = output

                if transaction.outputs[0].recipient != transaction.recipient:
                    print("Transaction output recipient is not who it should be on transaction %d" % i)
                    return False

                if transaction.get_inputs_value() != transaction.outputs[0].value \
                    and transaction.outputs[1].recipient != transaction.sender:

                    print("Transaction ouput `change` is not sender on transaction %d" % i)
                    return False

                i += 1

        return True

    def last_block_hash(self):
        if self.blocks:
            return self.blocks[-1].hash
        else:
            return "0"

    def append_new_block(self, mine=True):

        block = Block(self.last_block_hash())

        if mine:
            block.mine(self.difficulty)
            print("Block mined: " + block.hash)

        self.append_block(block)

        return block

    def print(self):
        index = 0

        for block in self.blocks:
            print("Block %d" % index)
            block.print()

            index += 1
