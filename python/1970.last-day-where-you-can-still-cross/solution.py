# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/last-day-where-you-can-still-cross/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    row: int = deserialize("int", read_line())
    col: int = deserialize("int", read_line())
    cells: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().latestDayToCross(row, col, cells)
    print("\noutput:", serialize(ans, "integer"))