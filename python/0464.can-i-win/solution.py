# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/can-i-win/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    maxChoosableInteger: int = deserialize("int", read_line())
    desiredTotal: int = deserialize("int", read_line())
    ans = Solution().canIWin(maxChoosableInteger, desiredTotal)
    print("\noutput:", serialize(ans, "boolean"))
