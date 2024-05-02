# Created by asetti2002 at 2024/04/25 20:29
# leetgo: 1.4.3
# https://leetcode.com/problems/get-watched-videos-by-your-friends/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        import collections
        q = collections.deque([(id, 0)])
        visited = {id}
        friends_set = set(friends[id])
        while q:
            cur, l = q.popleft()
            if l == level:
                cnt = collections.Counter([v for f in friends_set for v in watchedVideos[f]])
                return sorted(cnt.keys(), key=lambda x: (cnt[x], x))
            for f in friends[cur]:
                if f not in visited:
                    visited.add(f)
                    q.append((f, l + 1))
                    friends_set.update(friends[f])
        return []
# @lc code=end

if __name__ == "__main__":
    watchedVideos: List[List[str]] = deserialize("List[List[str]]", read_line())
    friends: List[List[int]] = deserialize("List[List[int]]", read_line())
    id: int = deserialize("int", read_line())
    level: int = deserialize("int", read_line())
    ans = Solution().watchedVideosByFriends(watchedVideos, friends, id, level)
    print("\noutput:", serialize(ans, "string[]"))
