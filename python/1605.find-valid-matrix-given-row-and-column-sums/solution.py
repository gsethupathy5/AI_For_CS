# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    rowSum: List[int] = deserialize("List[int]", read_line())
    colSum: List[int] = deserialize("List[int]", read_line())
    ans = Solution().restoreMatrix(rowSum, colSum)
    print("\noutput:", serialize(ans, "integer[][]"))
