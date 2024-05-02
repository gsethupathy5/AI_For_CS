# Created by asetti2002 at 2024/04/25 20:01
# leetgo: 1.4.3
# https://leetcode.com/problems/shortest-path-in-binary-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int: 
        import heapq
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        heap = [(1, 0, 0)]
        while heap:
            dist, i, j = heapq.heappop(heap)
            if i == n - 1 and j == n - 1:
                return dist
            for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    heapq.heappush(heap, (dist + 1, x, y))
                    grid[x][y] = 1
        return -1
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().shortestPathBinaryMatrix(grid)
    print("\noutput:", serialize(ans, "integer"))
