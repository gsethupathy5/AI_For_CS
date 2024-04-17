# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().isPossibleToCutPath(grid)
    print("\noutput:", serialize(ans, "boolean"))
