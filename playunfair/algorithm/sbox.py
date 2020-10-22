from playunfair.algorithm import playunfair

def encrypt(sbox, block):
    sboxInt = []
    for row in sbox:
        sboxIntRow = []
        for el in row:
            sboxIntRow.append(int(el, 16))
        sboxInt.append(sboxIntRow)
    cipher = []
    for byte in block:
        row = byte // 16
        col = byte % 16
        cipher.append(sboxInt[row][col])
    return cipher

def decrypt(sbox, block):
    sboxInt = []
    for row in sbox:
        sboxIntRow = []
        for el in row:
            sboxIntRow.append(int(el, 16))
        sboxInt.append(sboxIntRow)
    sboxLaid = []
    for row in sboxInt:
        sboxLaid = sboxLaid + row
    plain = []
    for byte in block:
        idx = sboxLaid.index(byte)
        row = idx // 16
        col = idx % 16
        plain.append(row * 16 + col)
    return plain
