# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/peak-index-in-a-mountain-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().peakIndexInMountainArray(arr)
    print("\noutput:", serialize(ans, "integer"))
