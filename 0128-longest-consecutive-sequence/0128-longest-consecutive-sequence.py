class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums) # Not to make any duplicates [2,3,4,4,5,10,20] => {2,3,4,5,10,20}
        for num in numset:
            if num-1 not in numset: #ex. 2 or 10 or 20
                length = 1
                while num+length in numset:
                    length = length+1
                longest = max(longest,length)
        return longest
