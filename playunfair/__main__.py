from playunfair.utils import files, operations
from playunfair.algorithm import cbc, ctr, ecb, easyEncrypt, feistel, playunfair, sbox
from playunfair.constants import feistel as feistelConstants
from playunfair.constants import sbox as sboxConstants

if __name__ == '__main__':
    print('Hello world!')
    
    # print("CBC")
    # data = files.openFile(".gitignore")
    # print([el for el in data[:12]])
    # blocks = files.splitToBlocks(3, data)
    # key = [255, 255, 255]
    # initialVector = [0, 0, 0]
    # cipher = cbc.encrypt(key, initialVector, blocks, easyEncrypt.encrypt)
    # newData = files.joinBlocks(cipher)
    # print(newData[:12])
    # plainBlocks = cbc.decrypt(key, initialVector, cipher, easyEncrypt.encrypt)
    # plainData = files.joinBlocks(plainBlocks)
    # print(plainData[:12])

    # print("ECB")
    # data = files.openFile(".gitignore")
    # print([el for el in data[:12]])
    # blocks = files.splitToBlocks(3, data)
    # key = [255, 255, 255]
    # cipher = ecb.encrypt(key, blocks, easyEncrypt.encrypt)
    # newData = files.joinBlocks(cipher)
    # print(newData[:12])
    # plainBlocks = ecb.decrypt(key, cipher, easyEncrypt.encrypt)
    # plainData = files.joinBlocks(plainBlocks)
    # print(plainData[:12])

    # print("CTR")
    # data = files.openFile(".gitignore")
    # print([el for el in data[:12]])
    # blocks = files.splitToBlocks(3, data)
    # key = [255, 255, 255]
    # cipher = ctr.encrypt(key, blocks, easyEncrypt.encrypt)
    # newData = files.joinBlocks(cipher)
    # print(newData[:12])
    # plainBlocks = ctr.decrypt(key, cipher, easyEncrypt.encrypt)
    # plainData = files.joinBlocks(plainBlocks)
    # print(plainData[:12])

    # print("FSTL")
    # data = files.openFile(".gitignore")
    # print([el for el in data[:12]])
    # blocks = files.splitToBlocks(8, data)
    # key = [0, 0, 0, 0, 255, 0, 255, 0]
    # cipher = feistel.encrypt(key, blocks, playunfair.encryptFeistel)
    # newData = files.joinBlocks(cipher)
    # print(newData[:12])
    # plainBlocks = feistel.decrypt(key, cipher, playunfair.encryptFeistel)
    # plainData = files.joinBlocks(plainBlocks)
    # print(plainData[:12])

    # print("PLFR")
    # data = files.openFile(".gitignore")
    # print([el for el in data[:8]])
    # blocks = files.splitToBlocks(8, data)
    # table = playunfair.createTable([3, 2, 45, 11, 2, 3])
    # cipher = playunfair.encryptPlayfair(table, blocks[0])
    # print(cipher)
    # plainBlock = playunfair.decryptPlayfair(table, cipher)
    # print(plainBlock)

    # print("SBOX")
    # data = files.openFile(".gitignore")
    # print([el for el in data[:8]])
    # blocks = files.splitToBlocks(8, data)
    # cipher = sbox.encrypt(sboxConstants.AES_MATRIX, blocks[0])
    # print(cipher)
    # plainBlock = sbox.decrypt(sboxConstants.AES_MATRIX, cipher)
    # print(plainBlock)
