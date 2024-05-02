# Created by asetti2002 at 2024/04/25 19:49
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-for-tickets/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        for i in range(1, days[-1] + 1):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(i-1, 0)] + costs[0], dp[max(i-7, 0)] + costs[1], dp[max(i-30, 0)] + costs[2])
        return dp[days[-1]]
# @lc code=end

if __name__ == "__main__":
    days: List[int] = deserialize("List[int]", read_line())
    costs: List[int] = deserialize("List[int]", read_line())
    ans = Solution().mincostTickets(days, costs)
    print("\noutput:", serialize(ans, "integer"))
