class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ml=0

        for i in s:
            if i-1 not in s:
                cl=1
                while i+cl in s:
                    cl+=1
                ml=max(ml, cl)
        
        return ml
            

        