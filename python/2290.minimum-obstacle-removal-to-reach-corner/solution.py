# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumObstacles(grid)
    print("\noutput:", serialize(ans, "integer"))