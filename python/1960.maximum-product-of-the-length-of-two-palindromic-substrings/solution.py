# Created by asetti2002 at 2024/04/25 20:18
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxProduct(self, s: str) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maxProduct(s)
    print("\noutput:", serialize(ans, "long"))
