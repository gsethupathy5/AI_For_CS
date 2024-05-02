# Created by asetti2002 at 2024/04/25 20:31
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left, right = max(i - r, 0), min(i + r, n)
            dp[left] = max(dp[left], right - left)
        
        ans = 0
        right, next_right = 0, 0
        
        for i in range(n + 1):
            if i > right:
                return -1
            if i > next_right:
                ans += 1
                right = next_right
            next_right = max(next_right, i + dp[i])
        
        return ans
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ranges: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minTaps(n, ranges)
    print("\noutput:", serialize(ans, "integer"))
