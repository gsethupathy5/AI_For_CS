# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/matrix-block-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().matrixBlockSum(mat, k)
    print("\noutput:", serialize(ans, "integer[][]"))
