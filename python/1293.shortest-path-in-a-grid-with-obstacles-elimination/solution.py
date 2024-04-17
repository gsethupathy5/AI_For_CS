# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().shortestPath(grid, k)
    print("\noutput:", serialize(ans, "integer"))
