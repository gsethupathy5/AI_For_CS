# Created by asetti2002 at 2024/05/01 19:58
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-common-factors/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        def common_factors_count(a, b):
            n = gcd(a, b)
            count = 0
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    count += 2
                    if i == n // i:
                        count -= 1
            return count
        
        return common_factors_count(a, b)
# @lc code=end

if __name__ == "__main__":
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    ans = Solution().commonFactors(a, b)
    print("\noutput:", serialize(ans, "integer"))
