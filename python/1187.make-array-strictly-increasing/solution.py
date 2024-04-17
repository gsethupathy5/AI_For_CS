# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/make-array-strictly-increasing/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    arr1: List[int] = deserialize("List[int]", read_line())
    arr2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().makeArrayIncreasing(arr1, arr2)
    print("\noutput:", serialize(ans, "integer"))
