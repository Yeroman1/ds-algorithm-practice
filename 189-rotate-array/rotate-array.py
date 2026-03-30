class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)

        l,h=0,len(nums)-1
        while l<h: nums[l],nums[h]=nums[h],nums[l];l+=1;h-=1
        l,h=0,k-1
        while l<h: nums[l],nums[h]=nums[h],nums[l];l+=1;h-=1
        l,h=k,len(nums)-1
        while l<h: nums[l],nums[h]=nums[h],nums[l];l+=1;h-=1