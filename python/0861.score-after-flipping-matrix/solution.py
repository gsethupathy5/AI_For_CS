# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/score-after-flipping-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().matrixScore(grid)
    print("\noutput:", serialize(ans, "integer"))