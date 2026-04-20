from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter=[]
        c=Counter(nums2)

        for i in nums1:
            if c[i] > 0:
                inter.append(i)
                c[i]-=1
            
        return inter