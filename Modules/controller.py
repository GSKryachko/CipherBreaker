import json

from Modules.cipherAnalyzer import CipherAnalyzer
from Modules.encryptor import Encryptor
from Modules.filesReader import FilesReader
from Modules.masksBuilder import MasksBuilder
from Modules.textCleaner import TextCleaner
from Modules.textsAnalyzer import TextsAnalyzer


class Controller:
    @staticmethod
    def encrypt(source, dest, chiper):
        encryptor = Encryptor(chiper)
        new_text = []
        with open(source, 'r', encoding='UTF-8') as source:
            for line in source:
                new_text.append(encryptor.replace(line, chiper))
        with open(dest, 'w+', encoding='UTF-8') as destination:
            destination.write(''.join(new_text))
            print("Encrypted text was saved to ", dest)
    
    @staticmethod
    def get_key(encrypted_text, masks, path_to_key, path_to_stats, alphabet):
        with open(masks, 'r', encoding='UTF-8') as f:
            masks = json.loads(f.read())
        cipher_analyzer = CipherAnalyzer(masks, path_to_stats,
                                         alphabet)
        with open(encrypted_text, 'r', encoding='UTF-8') as encrypted_text:
            text = TextCleaner.clean_text(encrypted_text.read().split(' '),
                                          alphabet)
            cipher = cipher_analyzer.analyze_using_lists(text)
        with open(path_to_key, 'w', encoding='UTF-8') as key_file:
            json.dump(cipher, key_file)
            print("Key saved to ", path_to_key)
    
    @staticmethod
    def build_masks(vocabulary, path_to_masks, alphabet):
        with open(vocabulary, 'r', encoding='UTF-8') as source:
            text = TextCleaner.clean_text(source.read(), alphabet.value)
            masks = MasksBuilder.build_masks(text, alphabet)
    
        with open(path_to_masks, 'w+', encoding='UTF-8') as destination:
            json.dump(masks, destination)
            print("Masks saved to", path_to_masks)
    
    @staticmethod
    def decrypt(encrytpted_text, decrypted_text, path_to_key):
        with open(path_to_key, 'r', encoding='UTF-8') as key:
            cipher = json.load(key)
        return Controller.encrypt(encrytpted_text, decrypted_text, cipher)

    @staticmethod
    def analyze(texts_dir, stats_file, alphabet):
        text = FilesReader.get_words(texts_dir)
        clean_text = TextCleaner.clean_text(text, alphabet)
        text_analyzer = TextsAnalyzer(alphabet)
        text_analyzer.analyze(clean_text)
        text_analyzer.stats.save(stats_file)
        print("Stats saved to {0}".format(stats_file))
