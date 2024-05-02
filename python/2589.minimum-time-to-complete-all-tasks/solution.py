# Created by asetti2002 at 2024/05/01 20:16
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: (x[1], x[0]))
        result = 0
        end_time = 0
        for start, end, duration in tasks:
            result += max(0, start - end_time)
            result += duration
            end_time = max(end_time, end)
        return result
# @lc code=end

if __name__ == "__main__":
    tasks: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findMinimumTime(tasks)
    print("\noutput:", serialize(ans, "integer"))
