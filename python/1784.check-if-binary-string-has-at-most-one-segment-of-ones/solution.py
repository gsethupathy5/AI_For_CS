# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().checkOnesSegment(s)
    print("\noutput:", serialize(ans, "boolean"))