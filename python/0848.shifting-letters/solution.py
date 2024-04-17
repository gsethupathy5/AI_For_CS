# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/shifting-letters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    shifts: List[int] = deserialize("List[int]", read_line())
    ans = Solution().shiftingLetters(s, shifts)
    print("\noutput:", serialize(ans, "string"))
