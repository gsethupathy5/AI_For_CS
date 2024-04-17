# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-multiple-of-three/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    digits: List[int] = deserialize("List[int]", read_line())
    ans = Solution().largestMultipleOfThree(digits)
    print("\noutput:", serialize(ans, "string"))
