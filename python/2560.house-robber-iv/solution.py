# Created by asetti2002 at 2024/05/01 20:18
# leetgo: 1.4.3
# https://leetcode.com/problems/house-robber-iv/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(idx, remaining):
            if remaining == 0:
                return 0
            if idx >= len(nums):
                return float('inf')
            steal = dp(idx + 2, remaining - 1) + nums[idx]
            not_steal = dp(idx + 1, remaining)
            return min(steal, not_steal)
        
        return dp(0, k)
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minCapability(nums, k)
    print("\noutput:", serialize(ans, "integer"))
