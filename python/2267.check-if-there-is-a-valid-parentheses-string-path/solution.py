# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().hasValidPath(grid)
    print("\noutput:", serialize(ans, "boolean"))
