# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().largestSubmatrix(matrix)
    print("\noutput:", serialize(ans, "integer"))
