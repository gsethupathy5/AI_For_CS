# Created by asetti2002 at 2024/05/01 19:56
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-even-multiple/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def lcm(a, b):
            return a // gcd(a, b) * b
        
        ans = 1
        for i in range(1, n + 1):
            ans = lcm(ans, i)
        return ans
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().smallestEvenMultiple(n)
    print("\noutput:", serialize(ans, "integer"))
