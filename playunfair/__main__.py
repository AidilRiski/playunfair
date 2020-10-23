from playunfair.utils import files, operations
from playunfair.algorithm import cbc, ctr, ecb, easyEncrypt, feistel, playunfair, sbox
from playunfair.constants import feistel as feistelConstants
from playunfair.constants import sbox as sboxConstants
from playunfair.constants import cbc as cbcConstants
import argparse

def main(args):
    key = args.key
    filename = args.filename
    method = args.method
    encrypt = args.encrypt
    decrypt = args.decrypt

    data = files.openFile(filename)
    blocks = files.splitToBlocks(8, data)
    key = bytearray(key, 'utf-8')

    if encrypt:
        cipher = []
        if method == 'cbc':
            cipher = cbc.encrypt(key, cbcConstants.INITIAL_VECTOR, blocks, playunfair.networkEncrypt)
        elif method == 'ecb':
            cipher = ecb.encrypt(key, blocks, playunfair.networkEncrypt)
        elif method == 'ctr':
            cipher = ctr.encrypt(key, blocks, playunfair.networkEncrypt)
        newData = files.joinBlocks(cipher)
        files.writeFile(filename + '.cipher', bytearray(newData))
    elif decrypt:
        plain = []
        if method == 'cbc':
            plain = cbc.decrypt(key, cbcConstants.INITIAL_VECTOR, blocks, playunfair.networkEncrypt)
        elif method == 'ecb':
            plain = ecb.decrypt(key, blocks, playunfair.networkEncrypt)
        elif method == 'ctr':
            plain = ctr.decrypt(key, blocks, playunfair.networkEncrypt)
        newData = files.joinBlocks(plain)
        files.writeFile(filename + '.plain', bytearray(newData))

def checkArgs(args):
    if args.encrypt and args.decrypt:
        raise Exception('cannot encrypt and decrypt at the same time')
    elif not args.encrypt and not args.decrypt:
        raise Exception('specify whether you are decrypting or encrypting')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="PlayUnfair Cipher"
    )

    parser.add_argument('method', choices=['cbc', 'ecb', 'ctr'], help='specify the method to use', action='store')
    parser.add_argument('key', help='specify the key to use', action='store')
    parser.add_argument('filename', help='specify the filename', action='store')
    parser.add_argument('-e', '--encrypt', help='encrypt the file using the keyword', action='store_true')
    parser.add_argument('-d', '--decrypt', help='decrypt the file using the keyword', action='store_true')

    args = parser.parse_args()

    try:
        checkArgs(args)
        main(args)
    except Exception as e:
        parser.error(e)
