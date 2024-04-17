# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/letter-tile-possibilities/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    tiles: str = deserialize("str", read_line())
    ans = Solution().numTilePossibilities(tiles)
    print("\noutput:", serialize(ans, "integer"))
