class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result,subset = [],[]

        def help(i):
            if i >= len(nums):
                result.append(subset.copy())
                return result
            subset.append(nums[i])
            help(i+1)
            subset.pop()

            help(i+1)
            
        help(0)
        return result 
            