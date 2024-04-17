# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/path-with-minimum-effort/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

# @lc code=end

if __name__ == "__main__":
    heights: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumEffortPath(heights)
    print("\noutput:", serialize(ans, "integer"))
