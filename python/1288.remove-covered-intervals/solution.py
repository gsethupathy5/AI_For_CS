# Created by asetti2002 at 2024/04/25 20:04
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-covered-intervals/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 1
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][1] > end:
                count += 1
                end = intervals[i][1]
        return count
# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().removeCoveredIntervals(intervals)
    print("\noutput:", serialize(ans, "integer"))
