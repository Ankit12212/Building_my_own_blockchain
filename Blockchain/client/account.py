import sys
sys.path.append('/Users/Ankit Regmi/OneDrive/Desktop/Bitcoin')
from Blockchain.Backend.Core.EllepticCurve.EllepticCurve import Sha256Point
from Blockchain.Backend.util.util import hash160, hash256
#from Blockchain.Backend.Core.database.database import AccountDB
import secrets

class account:
    def createKeys(self):
        Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
        Gy = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

        G = Sha256Point(Gx, Gy)

        self.privateKey = secrets.randbits(256)

        unCompressesPublicKey = self.privateKey * G
        xpoint = unCompressesPublicKey.x
        ypoint = unCompressesPublicKey.y

        if ypoint.num % 2 == 0:
            compressKey = b"/x02" + xpoint.num.to_bytes(32, "big")
        else:
            compressKey = b"/x03" + xpoint.num.to_bytes(32, "big")

        hsh160 = hash160(compressKey)

        main_prefix = b"/x00"

        newAddr =  main_prefix + hsh160

        checksum = hash256(newAddr)[:4]

        newAddr = newAddr + checksum

        BASE58_ALPAHBET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

        count = 0 
        for c in newAddr:
            if c == 0:
                count += 1
            else:
                break 

        num = int.from_bytes(newAddr, "big")
        prefix = '1' * count 

        result = ""

        while num > 0:
            num, mod = divmod(num, 58)
            result = BASE58_ALPAHBET[mod] + result 

        self.PublicAddress = prefix + result 

        print(f"Private Key {self.privateKey}")
        print(f"Public Key {self.PublicAddress}")
        print(f"Xpoint {xpoint} \n Ypoint {ypoint}")




if __name__ == "__main__":
    acct = account()
    acct.createKeys()
    #AccountDB().write([acct.__dict__])