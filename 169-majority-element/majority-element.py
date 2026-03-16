class Solution:
    def majorityElement(self, nums):
        appear = {}
        n = len(nums)

        for i in nums:
            if i in appear:
                appear[i]+=1
            else:    
                appear[i]=1
            if appear[i] > n // 2:
                return i
        