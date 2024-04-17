# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/integer-to-roman/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def intToRoman(self, num: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().intToRoman(num)
    print("\noutput:", serialize(ans, "string"))
