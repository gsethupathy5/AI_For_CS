# Created by asetti2002 at 2024/04/25 19:28
# leetgo: 1.4.3
# https://leetcode.com/problems/magic-squares-in-grid/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(i, j):
            s = ''.join(str(grid[i + x // 3][j + x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return grid[i + 1][j + 1] == 5 and sorted(s) == list('123456789')
        
        return sum(isMagic(i, j) for i in range(len(grid) - 2) for j in range(len(grid[0]) - 2))
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numMagicSquaresInside(grid)
    print("\noutput:", serialize(ans, "integer"))
