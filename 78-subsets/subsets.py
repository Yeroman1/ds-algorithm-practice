class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recur(start, path):
            result.append(path)
            for i in range(start, len(nums)):
                recur(i + 1, path + [nums[i]])

        result = []
        recur(0, [])
        return result