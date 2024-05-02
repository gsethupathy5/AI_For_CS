# Created by asetti2002 at 2024/05/01 20:21
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = [(0, 0, 0)]
        visited = set()
        
        while heap:
            time, x, y = heapq.heappop(heap)
            if x == n - 1 and y == m - 1:
                return time
            visited.add((x, y))
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < m and (new_x, new_y) not in visited:
                    new_time = max(time, grid[new_x][new_y])
                    heapq.heappush(heap, (new_time + 1, new_x, new_y))
        
        return -1
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumTime(grid)
    print("\noutput:", serialize(ans, "integer"))
