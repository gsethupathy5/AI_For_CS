# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/next-greater-numerically-balanced-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().nextBeautifulNumber(n)
    print("\noutput:", serialize(ans, "integer"))
