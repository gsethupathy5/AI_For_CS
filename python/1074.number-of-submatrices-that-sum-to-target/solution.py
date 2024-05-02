# Created by asetti2002 at 2024/04/25 19:59
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().numSubmatrixSumTarget(matrix, target)
    print("\noutput:", serialize(ans, "integer"))
