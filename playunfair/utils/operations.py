import numpy

def xorBlock(blockA, blockB):
    result = numpy.bitwise_xor(blockA, blockB)
    return result.tolist()
