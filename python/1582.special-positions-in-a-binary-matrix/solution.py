# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numSpecial(mat)
    print("\noutput:", serialize(ans, "integer"))
