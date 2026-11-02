class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def power(num):
            if num == 1:
                return True
            if num % 2 or num <= 0:
                return False
            return power(num // 2)

        return power(n)