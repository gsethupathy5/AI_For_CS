# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/transpose-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().transpose(matrix)
    print("\noutput:", serialize(ans, "integer[][]"))
