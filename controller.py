import json

from cipherAnalyzer import CipherAnalyzer
from encryptor import Encryptor
from masksBuilder import MasksBuilder
from textsAnalyzer import TextsAnalyzer


class Controller:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    @staticmethod
    def encrypt(source, dest, chiper):
        encryptor = Encryptor(chiper)
        new_text = []
        with open(source, 'r') as source:
            for line in source:
                new_text.append(encryptor.replace(line, chiper))
        with open(dest, 'w+') as destination:
            destination.write('\n'.join(new_text))
            print("Encrypted text was saved to ", dest)
    
    @staticmethod
    def get_key(encrypted_text, masks, path_to_key):
        with open(masks, 'r') as f:
            masks = json.loads(f.read())
        cipher_analyzer = CipherAnalyzer(masks, 'Stats/',
                                         'abcdefghijklmnopqrstuvwxyz')
        with open(encrypted_text, 'r') as encrypted_text:
            text = CipherAnalyzer.prepare_words(
                encrypted_text.read().replace('\n', ' '))
            cipher = cipher_analyzer.analyze_using_lists(text)
        with open(path_to_key, 'w') as key_file:
            json.dump(cipher, key_file)
            print("Key saved to ", path_to_key)
    
    @staticmethod
    def build_masks(vocabulary, path_to_masks):
        with open(vocabulary, 'r') as source:
            text = MasksBuilder.prepare_words(
                ' '.join(source.read().split('\n')))
            masks = MasksBuilder.build_masks(text)
        with open(path_to_masks, 'w+') as destination:
            json.dump(masks, destination)
            print("Masks saved to", path_to_masks)
    
    @staticmethod
    def decrypt(encrytpted_text, decrypted_text, path_to_key):
        with open(path_to_key, 'r') as key:
            cipher = json.load(key)
        return Controller.encrypt(encrytpted_text, decrypted_text, cipher)

    @staticmethod
    def analyze(texts_dir, stats_dir):
        text_analyzer = TextsAnalyzer(texts_dir)
        text_analyzer.analyze()
        text_analyzer.add_ngrams_to_stats()
        text_analyzer.add_words_with_masks_to_stats()
        text_analyzer.stats.save(stats_dir)
