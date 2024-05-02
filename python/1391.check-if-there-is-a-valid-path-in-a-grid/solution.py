# Created by asetti2002 at 2024/04/25 20:37
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        pass
# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().hasValidPath(grid)
    print("\noutput:", serialize(ans, "boolean"))
