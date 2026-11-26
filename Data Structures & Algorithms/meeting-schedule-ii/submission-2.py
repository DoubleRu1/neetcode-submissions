"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals_list = [(item.start,item.end) for item in intervals]
        intervals_list.sort(key=lambda x:x[0])
        visited = [False] * len(intervals_list)
        cnt = 0
        for i in range(len(intervals_list)):
            if not visited[i]:
                cnt += 1
                visited[i] = True
                cur = [intervals_list[i]]
                for j in range(i+1,len(intervals_list)):
                    if not visited[j] and intervals_list[j][0]>=cur[-1][1]:
                        cur.append(intervals_list[j])
                        visited[j] = True
                # print(visited)
                # print(cur)
        return cnt