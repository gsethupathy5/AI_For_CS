# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def digitCount(self, num: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    num: str = deserialize("str", read_line())
    ans = Solution().digitCount(num)
    print("\noutput:", serialize(ans, "boolean"))
