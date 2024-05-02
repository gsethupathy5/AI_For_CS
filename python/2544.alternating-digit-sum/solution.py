# Created by asetti2002 at 2024/05/01 20:12
# leetgo: 1.4.3
# https://leetcode.com/problems/alternating-digit-sum/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign = 1
        total = 0
        n = str(n)
        for digit in n:
            total += sign * int(digit)
            sign *= -1
        return total
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().alternateDigitSum(n)
    print("\noutput:", serialize(ans, "integer"))
