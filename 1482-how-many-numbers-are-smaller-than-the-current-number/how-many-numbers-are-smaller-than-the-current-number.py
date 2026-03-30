class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        r = {}

        for i, x in enumerate(s):
            if x not in r:
                r[x] = i

        return [r[x] for x in nums]