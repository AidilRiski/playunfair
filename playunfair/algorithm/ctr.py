from playunfair.utils import operations

def encrypt(key, blocks, encryptFunction):
    cipherBlocks = []
    blockSize = len(blocks[0])
    ctr = 0
    for i, block in enumerate(blocks):
        ctrBlock = ctr.to_bytes(blockSize, byteorder='big')
        encryptedCtrBlock = encryptFunction(key[i], ctrBlock)
        cipherBlock = operations.xorBlock(encryptedCtrBlock, block)
        cipherBlocks.append(cipherBlock)
        ctr += 1
    return cipherBlocks

def decrypt(key, blocks, decryptFunction):
    return encrypt(key, blocks, decryptFunction)
