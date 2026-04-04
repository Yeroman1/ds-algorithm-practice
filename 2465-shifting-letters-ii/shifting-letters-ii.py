class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        a=[0]*len(s)

        for l,r,d in shifts:
            a[l]+=1 if d==1 else -1    
            if r+1<len(a):
                a[r+1]-=1 if d==1 else -1

        for i in range(1, len(a)):
            a[i]=a[i-1]+a[i]

        res=""
        for i in range(len(s)):
            res+=chr((ord(s[i]) - ord('a') + a[i]) % 26 + ord('a'))
        
        return res