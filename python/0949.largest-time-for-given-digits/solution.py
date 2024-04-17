# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-time-for-given-digits/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().largestTimeFromDigits(arr)
    print("\noutput:", serialize(ans, "string"))
