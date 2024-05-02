# Created by asetti2002 at 2024/05/01 20:16
# leetgo: 1.4.3
# https://leetcode.com/problems/check-knight-tour-configuration/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        def is_valid_move(curr, next):
            diff = abs(curr[0] - next[0]), abs(curr[1] - next[1])
            return diff in {(1,2), (2,1)}
        n = len(grid)
        seen = set()
        for i in range(n):
            for j in range(n):
                seen.add(grid[i][j])
                if grid[i][j] == 0:
                    start = (i, j)
        if len(seen) != n*n or seen != set(range(n*n)):
            return False
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        for i in range(1, n*n):
            curr_num = i - 1
            curr_pos = divmod([x for row in grid for x in row].index(curr_num), n)
            next_num = i
            next_pos = divmod([x for row in grid for x in row].index(next_num), n)
            if not is_valid_move(curr_pos, next_pos):
                return False
        return True
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().checkValidGrid(grid)
    print("\noutput:", serialize(ans, "boolean"))
