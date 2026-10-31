class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letter_count = {}
        t_letter_count = {}

        if len(s) != len(t):
            return False

        for s_letter in s:
            if s_letter not in s_letter_count:
                s_letter_count[s_letter]=0
            s_letter_count[s_letter]+=1

        for t_letter in t:
            if t_letter not in t_letter_count:
                t_letter_count[t_letter]=0
            t_letter_count[t_letter]+=1

        if s_letter_count == t_letter_count:
            return True
        return False