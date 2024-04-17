# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    maze: List[List[str]] = deserialize("List[List[str]]", read_line())
    entrance: List[int] = deserialize("List[int]", read_line())
    ans = Solution().nearestExit(maze, entrance)
    print("\noutput:", serialize(ans, "integer"))
