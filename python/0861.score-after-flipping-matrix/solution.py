# Created by asetti2002 at 2024/04/25 19:32
# leetgo: 1.4.3
# https://leetcode.com/problems/score-after-flipping-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def toggle(row):
            return [1 - x for x in row] 
        
        m, n = len(grid), len(grid[0])
        res = m * (1 << (n - 1))
        
        for j in range(1, n):
            curr_one = sum(grid[i][j] == grid[i][0] for i in range(m))
            res += max(curr_one, m - curr_one) * (1 << (n - 1 - j))
        
        return res
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().matrixScore(grid)
    print("\noutput:", serialize(ans, "integer"))
