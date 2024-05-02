# Created by asetti2002 at 2024/04/25 20:14
# leetgo: 1.4.3
# https://leetcode.com/problems/ugly-number-iii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        def lcm(x, y):
            return x * y // gcd(x, y)

        def count_ugly_numbers(num, a, b, c, ab, ac, bc, abc):
            return num // a + num // b + num // c - num // ab - num // ac - num // bc + num // abc

        left, right = 1, 2 * 10**9
        ab, ac, bc = lcm(a, b), lcm(a, c), lcm(b, c)
        abc = lcm(ab, c)

        while left < right:
            mid = (left + right) // 2
            count = count_ugly_numbers(mid, a, b, c, ab, ac, bc, abc)
            if count < n:
                left = mid + 1
            else:
                right = mid

        return left
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    c: int = deserialize("int", read_line())
    ans = Solution().nthUglyNumber(n, a, b, c)
    print("\noutput:", serialize(ans, "integer"))
