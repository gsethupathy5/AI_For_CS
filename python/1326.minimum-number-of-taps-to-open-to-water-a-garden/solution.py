# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ranges: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minTaps(n, ranges)
    print("\noutput:", serialize(ans, "integer"))
