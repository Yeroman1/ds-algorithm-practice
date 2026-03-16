class Solution:
    def subsets(self, nums):
        a = [[]]
        for i in nums:
            a += [c + [i] for c in a]
        return a