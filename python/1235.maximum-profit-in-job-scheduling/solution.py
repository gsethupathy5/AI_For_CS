# Created by asetti2002 at 2024/04/25 20:20
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [[0, 0]]  # [time, profit]

        for s, e, p in jobs:
            i = bisect_right(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])

        return dp[-1][1]
# @lc code=end

if __name__ == "__main__":
    startTime: List[int] = deserialize("List[int]", read_line())
    endTime: List[int] = deserialize("List[int]", read_line())
    profit: List[int] = deserialize("List[int]", read_line())
    ans = Solution().jobScheduling(startTime, endTime, profit)
    print("\noutput:", serialize(ans, "integer"))
