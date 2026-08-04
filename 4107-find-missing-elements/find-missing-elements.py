class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        Range=set(range(min(nums), max(nums)+1))
        return sorted(list(Range-set(nums)))