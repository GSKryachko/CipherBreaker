class MasksBuilder:
    @staticmethod
    def build_masks(words, alphabet):
        masks = dict()
        for word in words:
            mask = MasksBuilder.build_mask(word, alphabet)
            if mask not in masks:
                masks[mask] = [word]
            else:
                masks[mask].append(word)
        return masks
    
    @staticmethod
    def build_mask(word, alphabet):
        substitution = dict()
        pointer = 0
        mask = ""
        for i in word:
            if i not in substitution:
                substitution[i] = alphabet.value[pointer]
                pointer += 1
            mask += substitution[i]
        return mask
