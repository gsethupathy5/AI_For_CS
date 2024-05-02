# Created by asetti2002 at 2024/04/25 20:36
# leetgo: 1.4.3
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = [min(row) for row in matrix]
        col_max = [max(col) for col in zip(*matrix)]
        return list(set(row_min) & set(col_max))
# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().luckyNumbers (matrix)
    print("\noutput:", serialize(ans, "integer[]"))
