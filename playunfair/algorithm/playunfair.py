from playunfair.utils import operations

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
    row = row % 16 if row < 0 or row > 16 else row
    col = col % 16 if col < 0 or col > 16 else col
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
