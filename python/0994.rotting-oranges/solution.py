# Created by asetti2002 at 2024/04/25 19:50
# leetgo: 1.4.3
# https://leetcode.com/problems/rotting-oranges/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().orangesRotting(grid)
    print("\noutput:", serialize(ans, "integer"))
