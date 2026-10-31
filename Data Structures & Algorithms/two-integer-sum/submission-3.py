class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Seen = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in Seen:
                return [Seen[difference], index]
            Seen[number]=index
        return False
            


        