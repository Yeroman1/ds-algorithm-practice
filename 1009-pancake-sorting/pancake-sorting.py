class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        r = []
        for i in range(len(arr)-1, 0, -1):
            j = arr.index(i+1)
            if j < i:
                if j > 0:
                    r.append(j+1)
                    arr[:j+1] = arr[:j+1][::-1]
                r.append(i+1)
                arr[:i+1] = arr[:i+1][::-1]
        return r
        