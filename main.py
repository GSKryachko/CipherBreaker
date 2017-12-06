import argparse
import json

from cipherAnalyzer import CipherAnalyzer
from cipherGenerator import CipherGenerator
from encryptor import Encryptor
from masksBuilder import MasksBuilder

parser = argparse.ArgumentParser()
parser.add_argument('source', metavar='source', type=str,
                    help="path to text file")

parser.add_argument('--decrypt', action='store_true',
                    default=False,
                    dest='decrypt',
                    help='decode text')

parser.add_argument('--analyze', action='store_true',
                    default=False,
                    dest='analyze',
                    help='Try to get key and print it to console')

parser.add_argument('--encrypt', action='store_true',
                    default=False,
                    dest='encrypt',
                    help='Try to get key and print it to console')

parser.add_argument('--build', action='store_true',
                    default=False,
                    dest='build',
                    help='Build masks and save to destination')

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
if args.build:
    with open(args.source, 'r') as source:
        text = Encryptor.prepare_words(' '.join(source.read().split('\n')))
        masks = MasksBuilder.build_masks(text)
    with open(args.dest, 'w+') as destination:
        json.dump(masks, destination)
        print("Masks saved to", args.dest)
if args.decrypt:
    with open('all_masks.txt', 'r') as f:
        masks = json.loads(f.read())
    cipherAnalyzer = CipherAnalyzer(masks)
    with open(args.source, 'r') as source:
        text = CipherAnalyzer.prepare_words(source.read().replace('\n', ' '))
        cipher = cipherAnalyzer.analyze_cipher_using_range(text)
        print(cipher)
        print(cipherAnalyzer.assumed_cipher)
        
    encryptor = Encryptor(cipher)
    new_text = []
    with open(args.source, 'r') as source:
        for line in source:
            text = Encryptor.prepare_words(line)
            new_text.extend(encryptor.encrypt(text))
    with open(args.dest, 'w+') as destination:
        destination.write(' '.join(new_text))
        print("Decrypted text was saved to ", args.dest)