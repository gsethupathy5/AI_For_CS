# Created by asetti2002 at 2024/04/25 20:16
# leetgo: 1.4.3
# https://leetcode.com/problems/where-will-the-ball-fall/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = [-1] * n
        
        for col in range(n):
            start = col
            
            for row in range(m):
                if grid[row][start] == 1:
                    if start + 1 < n and grid[row][start + 1] == 1:
                        start += 1
                    else:
                        break
                else:
                    if start - 1 >= 0 and grid[row][start - 1] == -1:
                        start -= 1
                    else:
                        break
            
            res[col] = start if row == m - 1 else -1
        
        return res
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findBall(grid)
    print("\noutput:", serialize(ans, "integer[]"))
