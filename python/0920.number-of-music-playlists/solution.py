# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-music-playlists/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    goal: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numMusicPlaylists(n, goal, k)
    print("\noutput:", serialize(ans, "integer"))
