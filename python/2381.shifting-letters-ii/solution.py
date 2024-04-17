# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/shifting-letters-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    shifts: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().shiftingLetters(s, shifts)
    print("\noutput:", serialize(ans, "string"))
