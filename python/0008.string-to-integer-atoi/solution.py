# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/string-to-integer-atoi/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def myAtoi(self, s: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().myAtoi(s)
    print("\noutput:", serialize(ans, "integer"))
