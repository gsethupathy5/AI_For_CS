# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/escape-a-large-maze/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    blocked: List[List[int]] = deserialize("List[List[int]]", read_line())
    source: List[int] = deserialize("List[int]", read_line())
    target: List[int] = deserialize("List[int]", read_line())
    ans = Solution().isEscapePossible(blocked, source, target)
    print("\noutput:", serialize(ans, "boolean"))
