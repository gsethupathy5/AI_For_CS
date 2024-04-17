# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-well-performing-interval/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    hours: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestWPI(hours)
    print("\noutput:", serialize(ans, "integer"))
