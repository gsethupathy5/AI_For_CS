# Created by asetti2002 at 2024/05/01 19:58
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-sum-of-an-hourglass/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = float('-inf')
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                hourglass_sum = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                max_sum = max(max_sum, hourglass_sum)
        return max_sum
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxSum(grid)
    print("\noutput:", serialize(ans, "integer"))
