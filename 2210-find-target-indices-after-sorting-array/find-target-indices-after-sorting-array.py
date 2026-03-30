class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        t=target
        r=[]
        for i,x in enumerate(nums):
            if x==t: r.append(i)

        return r 