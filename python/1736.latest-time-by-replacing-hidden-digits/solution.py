# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumTime(self, time: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    time: str = deserialize("str", read_line())
    ans = Solution().maximumTime(time)
    print("\noutput:", serialize(ans, "string"))
