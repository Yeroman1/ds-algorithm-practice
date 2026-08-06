import math
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while n:
            digits=[int(i) for i in list(str(n))]
            product=math.prod(digits)
            if product%t==0:
                return n
            n+=1