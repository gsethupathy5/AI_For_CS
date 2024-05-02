# Created by asetti2002 at 2024/04/25 19:41
# leetgo: 1.4.3
# https://leetcode.com/problems/flip-string-to-monotone-increasing/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        left_ones = [0] * (n+1)
        right_zeros = [0] * (n+1)
        
        for i in range(1, n+1):
            left_ones[i] = left_ones[i-1] + int(s[i-1] == '1')
        
        for i in range(n-1, -1, -1):
            right_zeros[i] = right_zeros[i+1] + int(s[i] == '0')
        
        min_flips = float('inf')
        
        for i in range(n+1):
            min_flips = min(min_flips, left_ones[i] + right_zeros[i])
        
        return min_flips
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minFlipsMonoIncr(s)
    print("\noutput:", serialize(ans, "integer"))
