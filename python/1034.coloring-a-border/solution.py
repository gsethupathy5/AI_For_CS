# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/coloring-a-border/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    row: int = deserialize("int", read_line())
    col: int = deserialize("int", read_line())
    color: int = deserialize("int", read_line())
    ans = Solution().colorBorder(grid, row, col, color)
    print("\noutput:", serialize(ans, "integer[][]"))
