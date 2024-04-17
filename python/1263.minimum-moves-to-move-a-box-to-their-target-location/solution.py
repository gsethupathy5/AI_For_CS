# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().minPushBox(grid)
    print("\noutput:", serialize(ans, "integer"))
