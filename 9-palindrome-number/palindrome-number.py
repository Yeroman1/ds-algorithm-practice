class Solution:
    def isPalindrome(self, x: int) -> bool:
        p=str(x)
        r=p[::-1]
        return p==r