class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={e:i for i,e in enumerate(nums1)}
        ans=[-1]*len(nums1)
        stack=[]

        for i in nums2[::-1]:
            while stack and stack[-1]<=i:
                stack.pop()
            if stack and i in d:
                ans[d[i]]=stack[-1]
            stack.append(i)
        return ans
