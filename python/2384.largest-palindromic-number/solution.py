# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-palindromic-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def largestPalindromic(self, num: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    num: str = deserialize("str", read_line())
    ans = Solution().largestPalindromic(num)
    print("\noutput:", serialize(ans, "string"))
