# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    p: int = deserialize("int", read_line())
    ans = Solution().minNonZeroProduct(p)
    print("\noutput:", serialize(ans, "integer"))
