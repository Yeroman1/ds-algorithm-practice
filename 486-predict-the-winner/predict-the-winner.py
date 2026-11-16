class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        seen = {}
        def solve(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            if (i, j) in seen:
                return seen[(i, j)]

            pick_left = nums[i] - solve(i + 1, j)
            pick_right = nums[j] - solve(i, j - 1)

            seen[(i, j)] = max(pick_left, pick_right)
            return seen[(i, j)]

        return solve(0, len(nums) - 1) >= 0