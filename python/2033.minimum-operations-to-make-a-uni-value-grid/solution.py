# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().minOperations(grid, x)
    print("\noutput:", serialize(ans, "integer"))
