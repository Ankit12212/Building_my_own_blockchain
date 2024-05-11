from Blockchain.Backend.util.util import hash256

class BlockHeader:
    def __init__(self, version, prevBlockHash, merkleRoot, timeStamp, bits):
        self.version = version 
        self.preBlockHash = prevBlockHash
        self.merkleRoot = merkleRoot
        self.timeStamp = timeStamp
        self.bits = bits
        self.nonce = 0 
        self.blockHash = ''

    def mine(self):
        while(self.blockHash[0:4]) != '0000':
            self.blockHash = hash256((str(self.version) + self.preBlockHash + self.merkleRoot + str(self.timeStamp) + self.bits + str(self.nonce)).encode()).hex()
            self.nonce += 1
            print(f"Mining Started {self.nonce}", end = '\r')