# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-local-values-in-a-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().largestLocal(grid)
    print("\noutput:", serialize(ans, "integer[][]"))
