# Created by asetti2002 at 2024/05/01 19:42
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        def num_trailing_zeros(num):
            count = 0
            while num % 10 == 0:
                count += 1
                num //= 10
            return count
        
        def dfs(i, j, visited, direction):
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j]:
                return 0
            visited[i][j] = True
            curr_num = grid[i][j]
            zeros = num_trailing_zeros(curr_num)
            if direction == 0:
                zeros += max(dfs(i+1, j, visited, 0), dfs(i-1, j, visited, 0))
            else:
                zeros += max(dfs(i, j+1, visited, 1), dfs(i, j-1, visited, 1))
            visited[i][j] = False
            return zeros
        
        max_zeros = 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                zeros = dfs(i, j, visited, 0)
                max_zeros = max(max_zeros, zeros)
                zeros = dfs(i, j, visited, 1)
                max_zeros = max(max_zeros, zeros)
        
        return max_zeros
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxTrailingZeros(grid)
    print("\noutput:", serialize(ans, "integer"))
