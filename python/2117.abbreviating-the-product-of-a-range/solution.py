# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/abbreviating-the-product-of-a-range/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().abbreviateProduct(left, right)
    print("\noutput:", serialize(ans, "string"))
