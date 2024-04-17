# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/01-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().updateMatrix(mat)
    print("\noutput:", serialize(ans, "integer[][]"))
