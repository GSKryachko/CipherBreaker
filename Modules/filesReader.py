import os


class FilesReader:
    @staticmethod
    def get_words(texts_dir):
        for text in os.listdir(texts_dir):
            for word in FilesReader.__get_words_from_file(texts_dir + text):
                yield word
                # return (word
                #         for text in os.listdir(texts_dir)
                #         for word in  FilesReader.__get_words_from_file(texts_dir + text))
    
    @staticmethod
    def __get_words_from_file(filename):
        with open(filename, 'r') as f:
            for line in f:
                for word in line.split(' '):
                    yield word
