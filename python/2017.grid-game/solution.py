# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/grid-game/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().gridGame(grid)
    print("\noutput:", serialize(ans, "long"))
