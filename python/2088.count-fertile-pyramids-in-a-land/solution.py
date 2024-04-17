# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPyramids(grid)
    print("\noutput:", serialize(ans, "integer"))
