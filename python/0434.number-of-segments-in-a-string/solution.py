# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-segments-in-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countSegments(self, s: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().countSegments(s)
    print("\noutput:", serialize(ans, "integer"))