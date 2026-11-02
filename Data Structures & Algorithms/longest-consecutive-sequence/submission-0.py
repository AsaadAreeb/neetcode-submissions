class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        NumberSet = set(nums)
        LongestSequence = 0
        for number in NumberSet:
            if (number - 1) not in NumberSet:
                CurrentLength = 1
                while (number + 1) in NumberSet:
                    number += 1
                    CurrentLength += 1
                LongestSequence = max(LongestSequence, CurrentLength)
        return LongestSequence