# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    events: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxValue(events, k)
    print("\noutput:", serialize(ans, "integer"))
