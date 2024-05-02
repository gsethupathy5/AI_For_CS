# Created by asetti2002 at 2024/04/25 19:03
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        dp[0][0] = 0
        max_val = nums[0]
        wasted = 0

        for i in range(1, n):
            max_val = max(max_val, nums[i])
            wasted += max_val * (i + 1) - sum(nums[:i + 1])

        dp[0][0] = wasted

        for i in range(1, n):
            for j in range(1, k + 1):
                min_res = float('inf')
                max_val = 0
                sum_num = 0

                for l in range(i, -1, -1):
                    max_val = max(max_val, nums[l])
                    sum_num += nums[l]

                    res = dp[l][j - 1] + max_val * (i - l + 1) - sum_num
                    min_res = min(min_res, res)

                dp[i][j] = min_res

        return dp[n - 1][k]
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minSpaceWastedKResizing(nums, k)
    print("\noutput:", serialize(ans, "integer"))
