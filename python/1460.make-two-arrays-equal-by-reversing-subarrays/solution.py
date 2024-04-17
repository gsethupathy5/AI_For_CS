# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    target: List[int] = deserialize("List[int]", read_line())
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canBeEqual(target, arr)
    print("\noutput:", serialize(ans, "boolean"))
