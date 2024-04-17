# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    number: str = deserialize("str", read_line())
    digit: str = deserialize("str", read_line())
    ans = Solution().removeDigit(number, digit)
    print("\noutput:", serialize(ans, "string"))
