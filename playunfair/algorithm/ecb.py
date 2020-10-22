def encrypt(key, blocks, encryptFunction):
    plainBlocks = []
    for block in blocks:
        cipherBlock = encryptFunction(key, block)
        plainBlocks.append(cipherBlock)
    return plainBlocks

def decrypt(key, blocks, decryptFunction):
    return encrypt(key, blocks, decryptFunction)
