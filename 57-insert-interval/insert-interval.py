class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        r = []
        for i in intervals:
            if i[1] < newInterval[0]:
                r.append(i)
            elif i[0] > newInterval[1]:
                r.append(newInterval)
                newInterval = i
            else:
                newInterval = [
                    min(newInterval[0], i[0]),
                    max(newInterval[1], i[1])
                ]
        r.append(newInterval)
        return r