class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        a = [0] * len(s)

        for l, r, d in shifts:
            val = 1 if d else -1
            a[l] += val
            if r + 1 < len(a):
                a[r + 1] -= val

        for i in range(1, len(a)):
            a[i] += a[i - 1]

        res = []
        for i in range(len(s)):
            res.append(chr((ord(s[i]) - ord('a') + a[i]) % 26 + ord('a')))

        return "".join(res)