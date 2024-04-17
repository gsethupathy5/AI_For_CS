# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/strictly-palindromic-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().isStrictlyPalindromic(n)
    print("\noutput:", serialize(ans, "boolean"))
