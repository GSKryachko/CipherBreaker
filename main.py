import argparse

from cipherGenerator import CipherGenerator
from controller import Controller

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

parser.add_argument('--masks', metavar='masks', type=str,
                    default=None,
                    help='key to encryption/decryption')
args = parser.parse_args()
alphabet = "abcdefghijklmnopqrstuvwxyz"

if args.encrypt:
    key = CipherGenerator.generate_cipher(alphabet)
    Controller.encrypt(args.source, args.dest, key)
if args.build:
    Controller.build_masks(args.source, args.dest)
if args.analyze:
    Controller.get_key(args.source, args.masks, args.key)
if args.decrypt:
    Controller.decrypt(args.source, args.dest, args.key)
