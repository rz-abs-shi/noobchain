from blockchain import Block, DIFFICULTY


class BlockChain:

    def __init__(self):
        self.blocks = []

    def append_block(self, block: Block):
        self.blocks.append(block)

    def check_valid(self):

        hash_prefix = "0" * DIFFICULTY

        prev_hash = "0"
        for block in self.blocks:
            if block.calculate_hash() != block.hash:
                return False

            if block.previous_hash != prev_hash:
                return False

            prev_hash = block.hash

            if not block.hash.startswith(hash_prefix):
                return False

        return True

    def last_block_hash(self):
        if self.blocks:
            return self.blocks[-1].hash
        else:
            return "0"

    def append_new_block(self, data: str, mine=True):

        block = Block(data, self.last_block_hash())

        if mine:
            block.mine(DIFFICULTY)
            print("Block mined :)")

        block.print()

        self.append_block(block)

        return block

    def print(self):
        index = 0

        for block in self.blocks:
            print("Block %d" % index)
            block.print()

            index += 1
