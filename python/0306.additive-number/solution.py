# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/additive-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    num: str = deserialize("str", read_line())
    ans = Solution().isAdditiveNumber(num)
    print("\noutput:", serialize(ans, "boolean"))
