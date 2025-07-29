class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        second_nums = [1]*len(nums)
        prefix = 1 
        for i in range(len(nums)):
            second_nums[i] = prefix
            prefix *= nums[i]
        suffix = 1 
        for i in range(len(nums)-1,-1,-1):
            second_nums[i] *= suffix
            suffix *= nums[i]
        return second_nums