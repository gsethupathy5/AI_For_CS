# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findSpecialInteger(arr)
    print("\noutput:", serialize(ans, "integer"))
