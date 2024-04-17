# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def modifyString(self, s: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().modifyString(s)
    print("\noutput:", serialize(ans, "string"))
