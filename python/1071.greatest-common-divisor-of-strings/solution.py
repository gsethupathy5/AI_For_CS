# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/greatest-common-divisor-of-strings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    str1: str = deserialize("str", read_line())
    str2: str = deserialize("str", read_line())
    ans = Solution().gcdOfStrings(str1, str2)
    print("\noutput:", serialize(ans, "string"))