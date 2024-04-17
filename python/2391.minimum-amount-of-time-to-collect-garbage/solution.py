# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    garbage: List[str] = deserialize("List[str]", read_line())
    travel: List[int] = deserialize("List[int]", read_line())
    ans = Solution().garbageCollection(garbage, travel)
    print("\noutput:", serialize(ans, "integer"))
