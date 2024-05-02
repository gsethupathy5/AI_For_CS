# Created by asetti2002 at 2024/05/01 19:43
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        obstacles = [[float('inf') for _ in range(n)] for _ in range(m)]
        
        obstacles[0][0] = 0
        
        queue = deque([(0, 0)])
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                
                if 0 <= new_x < m and 0 <= new_y < n:
                    new_obstacles = obstacles[x][y] + grid[new_x][new_y]
                    
                    if new_obstacles < obstacles[new_x][new_y]:
                        obstacles[new_x][new_y] = new_obstacles
                        queue.append((new_x, new_y))
        
        return obstacles[m - 1][n - 1] - grid[m-1][n-1]
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumObstacles(grid)
    print("\noutput:", serialize(ans, "integer"))
