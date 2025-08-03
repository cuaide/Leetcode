class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start =0
        max_len=0
        subset=set()
        for end in range(len(s)):
            while s[end] in subset:
                subset.remove(s[start])
                start+=1
            subset.add(s[end])
            max_len=max(max_len,end-start+1)
        return max_len

            
        