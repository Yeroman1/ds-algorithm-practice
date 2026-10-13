class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        ans = 0

        for p in prices:
            m = min(m, p)
            ans = max(ans, p - m)

        return ans