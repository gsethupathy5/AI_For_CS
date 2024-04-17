# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/matrix-diagonal-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().diagonalSum(mat)
    print("\noutput:", serialize(ans, "integer"))
