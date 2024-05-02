# Created by asetti2002 at 2024/04/25 20:00
# leetgo: 1.4.3
# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Write your code here
        pass
# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxEqualRowsAfterFlips(matrix)
    print("\noutput:", serialize(ans, "integer"))
