# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().minSumOfLengths(arr, target)
    print("\noutput:", serialize(ans, "integer"))
