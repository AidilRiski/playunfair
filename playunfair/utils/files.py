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
            counter = 0
            blocks.append(currentBlock)
    if counter != 0:
        diff = blockSize - counter
        while diff > 0:
            currentBlock.insert(0, 0)
            diff -= 1
        blocks.append(currentBlock)
    return blocks
