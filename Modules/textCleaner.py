import re


class TextCleaner:
    @staticmethod
    def clean_text(text, alphabet):
        pattern = '[^' + alphabet.value + '^' + alphabet.value.upper() + ']'
        for phrase in text:
            for word in re.sub(pattern, ' ', phrase).split(' '):
                word = word.lower()
                if TextCleaner.is_meaningful_word(word, alphabet):
                    yield word
    
    @staticmethod
    def is_meaningful_word(word, alphabet):
        if word == '':
            return False
        pattern = r'.*([' + alphabet.value + alphabet.value.upper() + r'])\1{3,}.*'
        if re.match(pattern, word):
            return False
        return True
