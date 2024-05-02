# Created by asetti2002 at 2024/05/01 20:10
# leetgo: 1.4.3
# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        row_sum = [0] * m
        col_sum = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_sum[i] += 1
                    col_sum[j] += 1
        diff = [[row_sum[i] + col_sum[j] - sum(grid[i]) - sum(row[j] for row in grid) for j in range(n)] for i in range(m)]
        return diff
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().onesMinusZeros(grid)
    print("\noutput:", serialize(ans, "integer[][]"))
