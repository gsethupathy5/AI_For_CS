# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/non-overlapping-intervals/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().eraseOverlapIntervals(intervals)
    print("\noutput:", serialize(ans, "integer"))