# Created by asetti2002 at 2024/04/25 20:32
# leetgo: 1.4.3
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countOrders(self, n: int) -> int:
        return (factorial(2 * n) // ((factorial(n) ** 2) * 2)) % (10**9 + 7)
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countOrders(n)
    print("\noutput:", serialize(ans, "integer"))
