class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Lookup = set()
        for Number in nums:
            if Number in Lookup:
                return True
            Lookup.add(Number)
        return False