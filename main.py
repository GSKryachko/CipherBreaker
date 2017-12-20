import argparse

from Modules.cipherGenerator import CipherGenerator
from controller import Controller

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='goal')

encrypt_parser = subparsers.add_parser('encrypt')
encrypt_parser.add_argument('source')
encrypt_parser.add_argument('destination')

decrypt_parser = subparsers.add_parser('decrypt')
decrypt_parser.add_argument('source')
decrypt_parser.add_argument('destination')
decrypt_parser.add_argument('key')

build_parser = subparsers.add_parser('build')
build_parser.add_argument('source')
build_parser.add_argument('destination')

get_key_parser = subparsers.add_parser('get_key')
get_key_parser.add_argument('text')
get_key_parser.add_argument('masks')
get_key_parser.add_argument('key')

encrypt_parser = subparsers.add_parser('analyze')
encrypt_parser.add_argument('texts')
encrypt_parser.add_argument('stats')

args = parser.parse_args()

alphabet = "abcdefghijklmnopqrstuvwxyz"
if args.goal == 'encrypt':
    key = CipherGenerator.generate_cipher(alphabet)
    Controller.encrypt(args.source, args.destination, key)
if args.goal == 'build':
    Controller.build_masks(args.source, args.destination)
if args.goal == 'get_key':
    Controller.get_key(args.text, args.masks, args.key)
if args.goal == 'decrypt':
    Controller.decrypt(args.source, args.destination, args.key)
if args.goal == 'analyze':
    Controller.analyze(args.texts, args.stats)
