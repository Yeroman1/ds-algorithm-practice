class Solution:
    def partitionLabels(self, s: str) -> List[int]:
       
        last = {c:i for i,c in enumerate(s)}
        a = []
        l = r = 0
        for i, c in enumerate(s):
            r = max(r, last[c])
            if i == r:
                a.append(r - l + 1)
                l = i + 1
        return a