def encrypt(key, blocks, encryptFunction):
    plainBlocks = []
    for i, block in enumerate(blocks):
        cipherBlock = encryptFunction(key[i], block)
        plainBlocks.append(cipherBlock)
    return plainBlocks

def decrypt(key, blocks, decryptFunction):
    return encrypt(key, blocks, decryptFunction)
