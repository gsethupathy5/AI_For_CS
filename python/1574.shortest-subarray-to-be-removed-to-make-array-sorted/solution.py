# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findLengthOfShortestSubarray(arr)
    print("\noutput:", serialize(ans, "integer"))
