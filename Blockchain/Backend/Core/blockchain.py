import sys 
sys.path.append('/Users/Ankit Regmi/OneDrive/Desktop/Bitcoin')

from Blockchain.Backend.Core.Block import Block 
from Blockchain.Backend.Core.blockheader import BlockHeader 
from Blockchain.Backend.util.util import hash256
from Blockchain.Backend.Core.database.database import BlockchainDB
import time 

ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain:
    def __init__(self):
        self.GenesisBlock() 

    def write_on_disk(self, block):
        blockchainDB = BlockchainDB()
        blockchainDB.write(block)

    def fetch_last_block(self):
        blockchainDB = BlockchainDB()
        return blockchainDB.lastBlock()

    def GenesisBlock(self):
        BlockHeight = 0 
        prevBlockcHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockcHash)

    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        Transaction =f"Ankit sent {BlockHeight} Bitcoins which he doesnot hold to Satoshi"
        merkleRoot = hash256(Transaction.encode()).hex()
        bits = 'ffff001f'
        blockheader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
        blockheader.mine()
        self.write_on_disk([Block(BlockHeight, 1, blockheader.__dict__, 1, Transaction).__dict__])

    def main(self): 
        while True: 
            lastBlock = self.fetch_last_block()
            BlockHeight = lastBlock["Height"]+1
            prevBlockHash = lastBlock['BlockHeader']['blockHash']
            self.addBlock(BlockHeight, prevBlockHash)

if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.main()