# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/detect-cycles-in-2d-grid/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().containsCycle(grid)
    print("\noutput:", serialize(ans, "boolean"))
