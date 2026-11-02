class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def power(num):
            if num==1:
                return True
            elif num<=0 or num%3!=0:
                return False
            return power(num//3)
        
        return power(n)