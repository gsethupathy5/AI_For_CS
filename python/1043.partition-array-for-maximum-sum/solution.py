# Created by asetti2002 at 2024/04/25 19:58
# leetgo: 1.4.3
# https://leetcode.com/problems/partition-array-for-maximum-sum/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            cur_max = 0
            for j in range(1, min(k, i + 1) + 1):
                cur_max = max(cur_max, arr[i - j + 1])
                dp[i] = max(dp[i], dp[i - j] + cur_max * j)
        return dp[-2]
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSumAfterPartitioning(arr, k)
    print("\noutput:", serialize(ans, "integer"))
