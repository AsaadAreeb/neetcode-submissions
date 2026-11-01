class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            letter_counts = {}
            for letter in word:
                if letter not in letter_counts:
                    letter_counts[letter] = 0
                letter_counts[letter] += 1
            key = tuple(sorted(letter_counts.items()))
        
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        return list(anagrams.values())


