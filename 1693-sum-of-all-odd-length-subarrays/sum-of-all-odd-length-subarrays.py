class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum=0
        p=[0]*(len(arr)+1)
        for i in range(1, len(p)):
            p[i]=arr[i-1]+p[i-1]
        for i in range(1, len(p)):
            j=i
            while j-1>=0:
                sum+=p[i]-p[j-1]
                j-=2
        return sum
