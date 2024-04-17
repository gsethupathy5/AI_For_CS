# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/escape-the-ghosts/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    ghosts: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: List[int] = deserialize("List[int]", read_line())
    ans = Solution().escapeGhosts(ghosts, target)
    print("\noutput:", serialize(ans, "boolean"))
