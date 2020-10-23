def vectorizeBlock(vector, block):
    vectorized = []
    for i in range(len(block)):
        vectorized.append(block[i] ^ vector[i])
    return vectorized

def encrypt(key, initialVector, blocks, encryptFunction):
    cipherBlocks = []
    currentVector = initialVector
    for i, block in enumerate(blocks):
        vectorized = vectorizeBlock(currentVector, block)
        cipherBlock = encryptFunction(key[i], vectorized)
        cipherBlocks.append(cipherBlock)
        currentVector = cipherBlock
    return cipherBlocks

def decrypt(key, initialVector, blocks, decryptFunction):
    plainBlocks = []
    currentVector = initialVector
    for i, block in enumerate(blocks):
        plainBlock = decryptFunction(key[i], block)
        plainBlock = vectorizeBlock(currentVector, plainBlock)
        plainBlocks.append(plainBlock)
        currentVector = block
    return plainBlocks
