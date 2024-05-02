# Created by asetti2002 at 2024/05/01 19:56
# leetgo: 1.4.3
# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        def merge(intervals):
            intervals.sort(key=lambda x: x[0])
            merged = [intervals[0]]
            for i in range(1, len(intervals)):
                if intervals[i][0] <= merged[-1][1]:
                    merged[-1][1] = max(intervals[i][1], merged[-1][1])
                else:
                    merged.append(intervals[i])
            return merged

        merged_intervals = merge(intervals)
        return len(merged_intervals)
# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minGroups(intervals)
    print("\noutput:", serialize(ans, "integer"))
