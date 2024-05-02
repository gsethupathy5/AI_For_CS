# Created by asetti2002 at 2024/04/25 19:34
# leetgo: 1.4.3
# https://leetcode.com/problems/nth-magical-number/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10**9 + 7
        lcm_ab = a * b // math.gcd(a, b)
        left = 1
        right = 10**14
        while left < right:
            mid = (left + right) // 2
            magic_num = mid // a + mid // b - mid // lcm_ab
            if magic_num < n:
                left = mid + 1
            else:
                right = mid
        return left % mod
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    ans = Solution().nthMagicalNumber(n, a, b)
    print("\noutput:", serialize(ans, "integer"))
