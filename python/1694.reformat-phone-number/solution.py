# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/reformat-phone-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reformatNumber(self, number: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    number: str = deserialize("str", read_line())
    ans = Solution().reformatNumber(number)
    print("\noutput:", serialize(ans, "string"))
