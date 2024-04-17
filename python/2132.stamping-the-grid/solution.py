# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/stamping-the-grid/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    stampHeight: int = deserialize("int", read_line())
    stampWidth: int = deserialize("int", read_line())
    ans = Solution().possibleToStamp(grid, stampHeight, stampWidth)
    print("\noutput:", serialize(ans, "boolean"))
