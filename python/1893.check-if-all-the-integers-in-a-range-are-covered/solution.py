# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    ranges: List[List[int]] = deserialize("List[List[int]]", read_line())
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().isCovered(ranges, left, right)
    print("\noutput:", serialize(ans, "boolean"))
