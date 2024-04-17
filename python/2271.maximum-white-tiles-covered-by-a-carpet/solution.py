# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    tiles: List[List[int]] = deserialize("List[List[int]]", read_line())
    carpetLen: int = deserialize("int", read_line())
    ans = Solution().maximumWhiteTiles(tiles, carpetLen)
    print("\noutput:", serialize(ans, "integer"))
