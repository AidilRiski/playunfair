import numpy

from playunfair.constants.feistel import (
    PERMUTATION_MATRIX_1,
    PERMUTATION_MATRIX_2,
    SHIFT_AMOUNT,
)

from playunfair.utils import operations

def generateRoundKeys(initialKeyBlock):
    if len(initialKeyBlock) != 8:
        raise Exception('Invalid initial key length! Length must be 64 bits (8 bytes)!')
    firstPermutationBits = operations.permutate(PERMUTATION_MATRIX_1, initialKeyBlock)
    keys = []
    ci = firstPermutationBits[0]
    di = firstPermutationBits[0]
    for i in range(16):
        ci = numpy.roll(ci, SHIFT_AMOUNT[i]).tolist()
        di = numpy.roll(di, SHIFT_AMOUNT[i]).tolist()
        ck = operations.permutate([PERMUTATION_MATRIX_2[0]], operations.bitArrayToBytesBlock(ci + di))
        dk = operations.permutate([PERMUTATION_MATRIX_2[1]], operations.bitArrayToBytesBlock(ci + di))
        key = ck[0] + dk[0]
        keys.append(int(operations.joinBitArray(key), 2))
    return keys
