import argparse

from cipherAnalyzer import CipherAnalyzer
from cipherGenerator import CipherGenerator
from encryptor import Encryptor

parser = argparse.ArgumentParser()
parser.add_argument('source', metavar='source', type=str,
                    help="path to text file")

parser.add_argument('--decrypt', action='store_true',
                    default=False,
                    dest='play',
                    help='decode text')

parser.add_argument('--analyze', action='store_true',
                    default=False,
                    dest='analyze',
                    help='Try to get key and print it to console')

parser.add_argument('--encrypt', action='store_true',
                    default=False,
                    dest='encrypt',
                    help='Try to get key and print it to console')

parser.add_argument('--dest', metavar='destination', type=str,
                    default='decrypted.txt',
                    help="where to save decrypted file")

parser.add_argument('--key', metavar='key', type=str,
                    default=None,
                    help='key to encryption/decryption')

args = parser.parse_args()
alphabet = "abcdefghijklmnopqrstuvwxyz"
if args.analyze:
    print('key')
    pass
if args.encrypt:
    encryptor = Encryptor(CipherGenerator.generate_cipher(alphabet))
    new_text = []
    with open(args.source, 'r') as source:
        for line in source:
            text = Encryptor.prepare_words(line)
            new_text.extend(encryptor.encrypt(text))
    with open(args.dest, 'w+') as destination:
        destination.write(' '.join(new_text))
        print("Encrypted text was saved to ", args.dest)
