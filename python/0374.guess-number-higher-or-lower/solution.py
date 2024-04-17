# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/guess-number-higher-or-lower/

from typing import *
from leetgo_py import *

# @lc code=begin

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    pick: int = deserialize("int", read_line())
    ans = Solution().guessNumber(n, pick)
    print("\noutput:", serialize(ans, "integer"))
