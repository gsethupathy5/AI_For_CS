# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    bottom: int = deserialize("int", read_line())
    top: int = deserialize("int", read_line())
    special: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxConsecutive(bottom, top, special)
    print("\noutput:", serialize(ans, "integer"))
