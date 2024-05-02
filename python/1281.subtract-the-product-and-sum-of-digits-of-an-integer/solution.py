# Created by asetti2002 at 2024/04/25 20:26
# leetgo: 1.4.3
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        _sum = 0
        for digit in str(n):
            product *= int(digit)
            _sum += int(digit)
        return product - _sum
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().subtractProductAndSum(n)
    print("\noutput:", serialize(ans, "integer"))
