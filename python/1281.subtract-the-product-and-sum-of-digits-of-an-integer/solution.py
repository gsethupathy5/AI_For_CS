# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().subtractProductAndSum(n)
    print("\noutput:", serialize(ans, "integer"))
