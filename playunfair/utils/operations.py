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

def joinBitArray(array):
    return "".join(map(str, array))

def bitArrayToBytesBlock(array):
    block = []
    count = 0
    byte = []
    for bit in array:
        byte.append(bit)
        count += 1
        if count == 8:
            block.append(int(joinBitArray(byte), 2))
            count = 0
            byte = []
    if count != 0:
        while count < 8:
            byte.append(0)
            count += 1
        block.append(int(joinBitArray(byte), 2))
    return block

def repeatArrayUntilLength(length, array):
    newArray = []
    for i in range(length):
        newArray.append(array[i % len(array)])
    return newArray
