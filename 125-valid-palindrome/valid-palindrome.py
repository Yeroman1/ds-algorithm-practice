class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s:
            if i.isalnum():
                a+=i.lower()
        
        l,r=0,len(a)-1

        while l<r:
            if a[l]!=a[r]:
                return False
            l+=1
            r-=1

        return True        