def vectorizeBlock(vector, block):
    vectorized = []
    for i in range(len(block)):
        vectorized.append(block[i] ^ vector[i])
    return vectorized
