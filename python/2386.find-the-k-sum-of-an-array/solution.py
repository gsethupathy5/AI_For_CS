# Created by asetti2002 at 2024/05/01 19:53
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-k-sum-of-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        dp = [0] * (k + 1)
        dp[0] = 1

        for num in nums:
            for i in range(k, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[k]
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kSum(nums, k)
    print("\noutput:", serialize(ans, "long"))
