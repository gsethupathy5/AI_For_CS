# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/two-best-non-overlapping-events/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    events: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxTwoEvents(events)
    print("\noutput:", serialize(ans, "integer"))
