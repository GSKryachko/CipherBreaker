class MasksBuilder:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    @staticmethod
    def build_masks(words):
        masks = dict()
        for word in words:
            masks[word] = MasksBuilder.build_mask(word)
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
