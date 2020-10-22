def encrypt(key, block):
    cipherBlock = []
    for i in range(len(block)):
        cipherBlock.append(key[i] ^ block[i])
    return cipherBlock
