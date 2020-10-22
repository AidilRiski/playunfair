import numpy

def xorBlock(blockA, blockB):
    result = numpy.bitwise_xor(blockA, blockB)
    return result.tolist()

def permutate(permutationMatrix, block):
    permutationBits = []
    for row in permutationMatrix:
        permutationBitRow = []
        for bitN in row:
            bitMask = createMask(bitN % 8)
            byteIndex = byteOfBitN(bitN)
            operationResult = bitMask & block[byteIndex]
            operationResult = 1 if operationResult else 0
            permutationBitRow.append(operationResult)
        permutationBits.append(permutationBitRow)
    return permutationBits

def createMask(bitN):
    return 1 << bitN

def byteOfBitN(bitN):
    return bitN // 8
