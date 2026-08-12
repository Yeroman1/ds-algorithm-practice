class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans, st = 0, -1
        frqc = Counter()
        for end in range(len(nums)):
            frqc[nums[end]] += 1
            while frqc[nums[end]] > k:
                st += 1
                frqc[nums[st]] -= 1
            ans = max(ans, end - st)
        return ans