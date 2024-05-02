# Created by asetti2002 at 2024/04/25 20:24
# leetgo: 1.4.3
# https://leetcode.com/problems/greatest-sum-divisible-by-three/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        
        for num in nums:
            dp_new = dp.copy()
            for total in dp:
                dp_new[(total + num) % 3] = max(dp_new[(total + num) % 3], total + num)
            dp = dp_new
        
        return dp[0]
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSumDivThree(nums)
    print("\noutput:", serialize(ans, "integer"))
