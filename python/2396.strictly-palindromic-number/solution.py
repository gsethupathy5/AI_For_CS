# Created by asetti2002 at 2024/05/01 19:56
# leetgo: 1.4.3
# https://leetcode.com/problems/strictly-palindromic-number/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return n > 5
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().isStrictlyPalindromic(n)
    print("\noutput:", serialize(ans, "boolean"))
