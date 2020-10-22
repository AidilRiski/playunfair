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
