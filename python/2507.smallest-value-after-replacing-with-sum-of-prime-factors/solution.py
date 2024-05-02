# Created by asetti2002 at 2024/05/01 20:08
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def smallestValue(self, n: int) -> int:
        def prime_factors(num):
            i = 2
            factors = []
            while i * i <= num:
                if num % i:
                    i += 1
                else:
                    num //= i
                    factors.append(i)
            if num > 1:
                factors.append(num)
            return factors

        while len(prime_factors(n)) > 1:
            n = sum(prime_factors(n))
        return n
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().smallestValue(n)
    print("\noutput:", serialize(ans, "integer"))
