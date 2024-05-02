# Created by asetti2002 at 2024/04/25 19:45
# leetgo: 1.4.3
# https://leetcode.com/problems/regions-cut-by-slashes/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    grid: List[str] = deserialize("List[str]", read_line())
    ans = Solution().regionsBySlashes(grid)
    print("\noutput:", serialize(ans, "integer"))
