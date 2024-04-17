# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    threshold: int = deserialize("int", read_line())
    ans = Solution().maxSideLength(mat, threshold)
    print("\noutput:", serialize(ans, "integer"))
