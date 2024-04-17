# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-path-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minPathSum(grid)
    print("\noutput:", serialize(ans, "integer"))
