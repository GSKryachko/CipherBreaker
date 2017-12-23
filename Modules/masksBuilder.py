from collections import defaultdict


class MasksBuilder:
    @staticmethod
    def build_masks(words, alphabet):
        masks = defaultdict(list)
        for word in words:
            mask = MasksBuilder.build_mask(word, alphabet)
            masks[mask].append(word)
        return masks
    
    @staticmethod
    def build_mask(word, alphabet):
        substitution = {}
        pointer = 0
        mask = []
        for i in word:
            if i not in substitution:
                substitution[i] = alphabet.value[pointer]
                pointer += 1
            mask.append(substitution[i])
        return ''.join(mask)
