# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-difference/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().findTheDifference(s, t)
    print("\noutput:", serialize(ans, "character"))