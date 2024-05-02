# Created by asetti2002 at 2024/04/25 20:25
# leetgo: 1.4.3
# https://leetcode.com/problems/count-servers-that-communicate/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        count = 0
        rows = [0] * len(grid)
        cols = [0] * len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    count += 1
        
        return count
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countServers(grid)
    print("\noutput:", serialize(ans, "integer"))
