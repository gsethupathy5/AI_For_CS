# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/path-crossing/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    path: str = deserialize("str", read_line())
    ans = Solution().isPathCrossing(path)
    print("\noutput:", serialize(ans, "boolean"))
