class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
        # This problem requires the following conditions:
        # 1. Only consider the first k elements of nums.
        # 2. Do not create any additional lists.
