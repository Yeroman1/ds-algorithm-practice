class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c = msum = nums[0]

        for i in range(1, len(nums)):
            c = max(nums[i], c + nums[i])
            msum = max(msum, c)

        return msum