# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-frogs-croaking/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    croakOfFrogs: str = deserialize("str", read_line())
    ans = Solution().minNumberOfFrogs(croakOfFrogs)
    print("\noutput:", serialize(ans, "integer"))
