class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7

        def power(a,b):
            if b==0:
                return 1

            x=power(a,b//2)
            x=(x*x)%mod

            if b%2:
                x=(x*a)%mod

            return x

        return (power(5,(n+1)//2)*power(4,n//2))%mod