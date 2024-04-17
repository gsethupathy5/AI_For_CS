# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/count-sub-islands/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grid1: List[List[int]] = deserialize("List[List[int]]", read_line())
    grid2: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countSubIslands(grid1, grid2)
    print("\noutput:", serialize(ans, "integer"))
