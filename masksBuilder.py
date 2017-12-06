import re


class MasksBuilder:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    @staticmethod
    def build_masks(words):
        masks = dict()
        for word in words:
            mask = MasksBuilder.build_mask(word)
            if mask not in masks:
                masks[mask] = [word]
            else:
                masks[mask].append(word)
        return masks
    
    @staticmethod
    def build_mask(word):
        substitution = dict()
        pointer = 0
        mask = ""
        for i in word:
            if i not in substitution:
                substitution[i] = MasksBuilder.alphabet[pointer]
                pointer += 1
            mask += substitution[i]
        return mask

    @staticmethod
    def prepare_words(text):
        return [word.lower() for word in
                re.sub('[!@#$.,\'?:;`-]', '', text).split(' ')]
