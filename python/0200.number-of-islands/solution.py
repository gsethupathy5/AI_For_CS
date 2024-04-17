# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-islands/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    grid: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().numIslands(grid)
    print("\noutput:", serialize(ans, "integer"))
