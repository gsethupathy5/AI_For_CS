# Created by asetti2002 at 2024/05/01 20:07
# leetgo: 1.4.3
# https://leetcode.com/problems/delete-greatest-value-in-each-row/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        result = 0
        while grid:
            max_vals = [max(row) for row in grid]
            max_val = max(max_vals)
            result += max_val
            for i in range(len(grid)):
                if max_val in grid[i]:
                    grid[i].remove(max_val)
            grid = [row for row in grid if row]
        return result
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().deleteGreatestValue(grid)
    print("\noutput:", serialize(ans, "integer"))
