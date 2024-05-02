# Created by asetti2002 at 2024/05/01 20:04
# leetgo: 1.4.3
# https://leetcode.com/problems/count-ways-to-build-good-strings/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dp(length, zeros, ones):
            if length < low or length > high or zeros > zero or ones > one:
                return 0
            if length == high and zeros == zero and ones == one:
                return 1
            return (dp(length + 1, zeros, ones) + dp(length + 1, zeros + 1, ones) + dp(length + 1, zeros, ones + 1)) % MOD

        return dp(0, 0, 0)
# @lc code=end

if __name__ == "__main__":
    low: int = deserialize("int", read_line())
    high: int = deserialize("int", read_line())
    zero: int = deserialize("int", read_line())
    one: int = deserialize("int", read_line())
    ans = Solution().countGoodStrings(low, high, zero, one)
    print("\noutput:", serialize(ans, "integer"))
