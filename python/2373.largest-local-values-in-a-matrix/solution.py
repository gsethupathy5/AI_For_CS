# Created by asetti2002 at 2024/05/01 19:52
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-local-values-in-a-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = []
        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                local_values = [grid[a][b] for a in range(i, i + 3) for b in range(j, j + 3)]
                row.append(max(local_values))
            maxLocal.append(row)
        return maxLocal
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().largestLocal(grid)
    print("\noutput:", serialize(ans, "integer[][]"))
