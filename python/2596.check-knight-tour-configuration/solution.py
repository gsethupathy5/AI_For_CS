# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/check-knight-tour-configuration/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().checkValidGrid(grid)
    print("\noutput:", serialize(ans, "boolean"))
