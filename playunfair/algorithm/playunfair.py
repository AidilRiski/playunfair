from playunfair.utils import operations
from playunfair.algorithm import (
    feistel,
    sbox,
)
from playunfair.constants import sbox as sboxConstants
import numpy

def encryptFeistel(key, block):
    key = key.to_bytes(6, byteorder='big')
    lengthDiff = len(key) - len(block)
    if lengthDiff > 0:
        key = key[lengthDiff:]
    keyInt = []
    for el in key:
        keyInt.append(el)
    return operations.xorBlock(keyInt, block)

def createTable(key):
    key = list(dict.fromkeys(key))
    table = []
    for el in key:
        table.append(el)
    for i in range(256):
        if i not in table:
            table.append(i)
    return table

def getTableElement(row, col, table):
    row = row % 16 if row < 0 or row >= 16 else row
    col = col % 16 if col < 0 or col >= 16 else col
    return table[row * 16 + col]

def encryptPlayfair(table, block):
    cipherBlock = []
    i = 0
    while i < len(block):
        id1 = table.index(block[i])
        row1 = id1 // 16
        col1 = id1 % 16
        id2 = table.index(block[i + 1])
        row2 = id2 // 16
        col2 = id2 % 16
        pos = encryptPlayfairHelper(row1, col1, row2, col2)
        cipher1 = getTableElement(pos[0], pos[1], table)
        cipher2 = getTableElement(pos[2], pos[3], table)
        cipherBlock.append(cipher1)
        cipherBlock.append(cipher2)
        i += 2
    return cipherBlock

def encryptPlayfairHelper(row1, col1, row2, col2):
    if row1 == row2:
        return [row1, col1 + 1, row2, col2 + 1]
    elif col1 == col2:
        return [row1 + 1, col1, row2 + 1, col2]
    else:
        return [row2, col1, row1, col2]

def decryptPlayfair(table, block):
    plainBlock = []
    i = 0
    while i < len(block):
        id1 = table.index(block[i])
        row1 = id1 // 16
        col1 = id1 % 16
        id2 = table.index(block[i + 1])
        row2 = id2 // 16
        col2 = id2 % 16
        pos = decryptPlayfairHelper(row1, col1, row2, col2)
        plain1 = getTableElement(pos[0], pos[1], table)
        plain2 = getTableElement(pos[2], pos[3], table)
        plainBlock.append(plain1)
        plainBlock.append(plain2)
        i += 2
    return plainBlock

def decryptPlayfairHelper(row1, col1, row2, col2):
    if row1 == row2:
        return [row1, col1 - 1, row2, col2 - 1]
    elif col1 == col2:
        return [row1 - 1, col1, row2 - 1, col2]
    else:
        return [row2, col1, row1, col2]

def switchKey(key, block):
    return operations.xorBlock(key, block)

def cycleTable(key, table):
    for byte in key:
        if byte % 2 == 1:
            return numpy.roll(table, 1).tolist()
        else:
            reversedTable = []
            for row in table:
                reversedTable.append(numpy.roll(row, 1).tolist())
            return reversedTable

def networkEncrypt(key, block):
    sbox1 = createTable(key)
    sbox2 = cycleTable(key, sbox1)
    cipherBlock1 = encryptPlayfair(sbox1, block)
    cipherBlock2 = encryptPlayfair(sbox2, cipherBlock1)
    cipherBlock3 = sbox.encrypt(sboxConstants.AES_MATRIX, cipherBlock2)
    twoBytes = cipherBlock3[:2]
    sixBytes = cipherBlock3[2:]
    twoBytesFeistelResult = feistel.encrypt(key, twoBytes, encryptFeistel)
    sixBytesFeistelResult = feistel.encrypt(key, sixBytes, encryptFeistel)
    cipherBlock4 = twoBytesFeistelResult + sixBytesFeistelResult
    return cipherBlock4

def networkDecrypt(key, block):
    twoBytes = block[:2]
    sixBytes = block[2:]
    twoBytesFeistelResult = feistel.decrypt(key, twoBytes, encryptFeistel)
    sixBytesFeistelResult = feistel.decrypt(key, sixBytes, encryptFeistel)
    plainBlock1 = twoBytesFeistelResult + sixBytesFeistelResult
    plainBlock2 = sbox.decrypt(sboxConstants.AES_MATRIX, plainBlock1)
    sbox1 = createTable(key)
    sbox2 = cycleTable(key, sbox1)
    plainBlock3 = decryptPlayfair(sbox2, plainBlock2)
    plainBlock4 = decryptPlayfair(sbox1, plainBlock3)
    return plainBlock4
