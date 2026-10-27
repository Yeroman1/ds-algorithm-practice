class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                smaller_num = stack.pop()
                next_greater[smaller_num] = num
            
            stack.append(num)
            
        for num in stack:
            next_greater[num] = -1
            
        return [next_greater[num] for num in nums1]

