# Created by asetti2002 at 2024/05/01 19:49
# leetgo: 1.4.3
# https://leetcode.com/problems/equal-row-and-column-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            if grid[i] in zip(*grid):
                count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().equalPairs(grid)
    print("\noutput:", serialize(ans, "integer"))
