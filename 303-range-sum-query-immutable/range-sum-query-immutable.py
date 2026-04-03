class NumArray:

    def __init__(self, nums: List[int]):
        self.p=[0]*(len(nums)+1)
        for i in range(1, len(nums)+1):
            self.p[i]=self.p[i-1]+nums[i-1]
            

    def sumRange(self, left: int, right: int) -> int:
        rsum=self.p[right+1]
        lsum=self.p[left]

        return rsum-lsum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)