# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/a-number-after-a-double-reversal/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().isSameAfterReversals(num)
    print("\noutput:", serialize(ans, "boolean"))
