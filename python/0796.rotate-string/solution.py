# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/rotate-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    goal: str = deserialize("str", read_line())
    ans = Solution().rotateString(s, goal)
    print("\noutput:", serialize(ans, "boolean"))