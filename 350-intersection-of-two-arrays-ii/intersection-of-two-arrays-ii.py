class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter=[]
        s, l = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)

        for i in s:
            if i in l:
                inter.append(i)
                l.remove(i)
            
        return inter