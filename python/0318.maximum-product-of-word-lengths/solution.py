# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-product-of-word-lengths/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().maxProduct(words)
    print("\noutput:", serialize(ans, "integer"))
