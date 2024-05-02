# Created by asetti2002 at 2024/04/25 20:17
# leetgo: 1.4.3
# https://leetcode.com/problems/path-with-maximum-gold/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def backtrack(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            cell_gold = grid[i][j]
            grid[i][j] = 0
            max_gold = max(backtrack(i+1, j), backtrack(i-1, j), backtrack(i, j+1), backtrack(i, j-1))
            grid[i][j] = cell_gold
            return cell_gold + max_gold
        
        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, backtrack(i, j))
        
        return max_gold
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().getMaximumGold(grid)
    print("\noutput:", serialize(ans, "integer"))
