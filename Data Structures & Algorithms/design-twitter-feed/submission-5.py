import heapq
from typing import List

class Twitter:

    def __init__(self):
        # userId -> set of followeeIds
        self.follow_dict = {}
        # userId -> list of (time, tweetId)
        self.posts = {}
        # 全局时间戳，越大越新
        self.idx = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        p = self.posts.get(userId, [])
        # 用正的时间戳
        p.append((self.idx, tweetId))
        self.posts[userId] = p
        self.idx += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # 当前用户关注的人
        followed = list(self.follow_dict.get(userId, set()))
        # 加上自己
        followed.append(userId)
        # 去重（虽然后面用的是 set，但这里写一下更保险）
        followed = list(set(followed))

        heap = []
        # 把自己和关注的人的所有 tweet 都丢进一个小顶堆中
        for f in followed:
            for p in self.posts.get(f, []):
                heapq.heappush(heap, p)
                if len(heap) > 10:
                    # 始终只保留时间最“新”的 10 条
                    heapq.heappop(heap)

        ans = []
        while heap:
            # 现在从堆里弹出的是从“最旧”到“最新”
            ans.append(heapq.heappop(heap)[1])
        # 反转成从最新到最旧
        return ans[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        # 不能关注自己
        if followerId == followeeId:
            return
        s = self.follow_dict.get(followerId)
        if s is None:
            s = set()
            self.follow_dict[followerId] = s
        # set 自动去重
        s.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        s = self.follow_dict.get(followerId)
        if s is not None:
            # discard/判断后 remove 都行，这里写成判断后删
            if followeeId in s:
                s.remove(followeeId)
