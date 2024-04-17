# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-rows-covered-by-columns/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    numSelect: int = deserialize("int", read_line())
    ans = Solution().maximumRows(matrix, numSelect)
    print("\noutput:", serialize(ans, "integer"))
