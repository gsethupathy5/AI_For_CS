# Created by asetti2002 at 2024/04/25 20:15
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-magic-square/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 1
        
        sums = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                sums[i][j] = grid[i][j] + (sums[i][j - 1] if j > 0 else 0) + (sums[i - 1][j] if i > 0 else 0) - ((sums[i - 1][j - 1] if i > 0 and j > 0 else 0))
        
        def checkMagicSquare(i, j, size):
            magic_sum = sums[i + size - 1][j + size - 1] - (sums[i + size - 1][j - 1] if j > 0 else 0) - (sums[i - 1][j + size - 1] if i > 0 else 0) + ((sums[i - 1][j - 1] if i > 0 and j > 0 else 0))
            for k in range(size):
                if sums[i + k][j + size - 1] - (sums[i + k][j - 1] if j > 0 else 0) != magic_sum: return False
                if sums[i + size - 1][j + k] - (sums[i - 1][j + k] if i > 0 else 0) != magic_sum: return False
            diag1 = diag2 = True
            for k in range(size):
                diag1 &= grid[i + k][j + k] == grid[i][j]
                diag2 &= grid[i + size - 1 - k][j + k] == grid[i][j]
            return diag1 and diag2 and sum(grid[i][j:j+size]) == magic_sum
        
        for i in range(m):
            for j in range(n):
                for size in range(res + 1, min(m - i, n - j) + 1):
                    if checkMagicSquare(i, j, size):
                        res = size
        return res
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().largestMagicSquare(grid)
    print("\noutput:", serialize(ans, "integer"))
