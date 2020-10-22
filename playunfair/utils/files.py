def openFile(filename):
    file = open(filename, 'rb')
    return file.read()

def splitToBlocks(blockSize, data):
    blocks = []
    counter = 0
    currentBlock = []
    for byte in data:
        currentBlock.append(byte)
        counter += 1
        if counter == blockSize:
            blocks.append(currentBlock)
            counter = 0
            currentBlock = []
    if counter != 0:
        diff = blockSize - counter
        while diff > 0:
            currentBlock.append(0)
            diff -= 1
        blocks.append(currentBlock)
    return blocks

def joinBlocks(blocks):
    data = []
    for block in blocks:
        for byte in block:
            data.append(byte)
    return data
