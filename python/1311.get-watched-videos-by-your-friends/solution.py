# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/get-watched-videos-by-your-friends/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    watchedVideos: List[List[str]] = deserialize("List[List[str]]", read_line())
    friends: List[List[int]] = deserialize("List[List[int]]", read_line())
    id: int = deserialize("int", read_line())
    level: int = deserialize("int", read_line())
    ans = Solution().watchedVideosByFriends(watchedVideos, friends, id, level)
    print("\noutput:", serialize(ans, "string[]"))
