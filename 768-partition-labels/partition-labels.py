class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        r = []
        mx = start = 0
        for i, c in enumerate(s):
            mx = max(mx, last[c])
            if mx == i:
                r.append(i - start + 1)
                start = i + 1
        return r