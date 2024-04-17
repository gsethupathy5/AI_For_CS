# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    parent: List[int] = deserialize("List[int]", read_line())
    s: str = deserialize("str", read_line())
    ans = Solution().longestPath(parent, s)
    print("\noutput:", serialize(ans, "integer"))
