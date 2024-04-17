# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    candidates: List[int] = deserialize("List[int]", read_line())
    ans = Solution().largestCombination(candidates)
    print("\noutput:", serialize(ans, "integer"))
