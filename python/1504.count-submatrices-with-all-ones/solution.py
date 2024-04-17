# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/count-submatrices-with-all-ones/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numSubmat(mat)
    print("\noutput:", serialize(ans, "integer"))
