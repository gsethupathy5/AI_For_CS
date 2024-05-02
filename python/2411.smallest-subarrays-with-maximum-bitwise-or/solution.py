# Created by asetti2002 at 2024/05/01 19:57
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [n] * n
        nxt = [n] * 31
        for i in range(n-1, -1, -1):
            now = 0
            for j in range(30, -1, -1):
                if (nums[i] >> j) & 1:
                    if nxt[j] != n:
                        now = max(now, nxt[j])
                    nxt[j] = i
                if now != n:
                    ans[i] = min(ans[i], now - i + 1)
        return ans
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().smallestSubarrays(nums)
    print("\noutput:", serialize(ans, "integer[]"))
