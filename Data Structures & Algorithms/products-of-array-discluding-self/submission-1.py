class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        leftproduct = 1
        for index in range(len(nums)):
            result[index] = leftproduct
            leftproduct *= nums[index]

        rightproduct = 1
        for index in range(len(nums)-1, -1, -1):
            result[index] *= rightproduct
            rightproduct *= nums[index]
        
        return result
