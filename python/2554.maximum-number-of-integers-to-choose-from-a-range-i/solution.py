# Created by asetti2002 at 2024/05/01 20:14
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        dp = [0] * (maxSum + 1)
        res = 0
        for i in range(1, n+1):
            if i in banned:
                continue
            for j in range(maxSum, i-1, -1):
                dp[j] = max(dp[j], dp[j-i] + 1)
                res = max(res, dp[j])
        return res
# @lc code=end

if __name__ == "__main__":
    banned: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    maxSum: int = deserialize("int", read_line())
    ans = Solution().maxCount(banned, n, maxSum)
    print("\noutput:", serialize(ans, "integer"))
