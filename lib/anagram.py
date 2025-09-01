# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word
        self._sorted = sorted(word.lower())

    def match(self, candidates):
        base_lower = self.word.lower()
        matches = []
        for candidate in candidates:
            cand_lower = candidate.lower()
            if cand_lower == base_lower:
                continue
            if sorted(cand_lower) == self._sorted:
                matches.append(candidate)
        return matches
