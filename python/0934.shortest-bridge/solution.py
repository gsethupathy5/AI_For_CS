# Created by asetti2002 at 2024/04/25 19:42
# leetgo: 1.4.3
# https://leetcode.com/problems/shortest-bridge/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().shortestBridge(grid)
    print("\noutput:", serialize(ans, "integer"))
