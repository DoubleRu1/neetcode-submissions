class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        while idx < len(intervals):
            if intervals[idx][0]>newInterval[0]:
                break
            idx += 1
        intervals.insert(idx,newInterval)
        
        ans = []
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1],interval[1])
        return ans

