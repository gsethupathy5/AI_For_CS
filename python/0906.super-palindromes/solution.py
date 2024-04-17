# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/super-palindromes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    left: str = deserialize("str", read_line())
    right: str = deserialize("str", read_line())
    ans = Solution().superpalindromesInRange(left, right)
    print("\noutput:", serialize(ans, "integer"))
