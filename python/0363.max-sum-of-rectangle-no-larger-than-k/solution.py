# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSumSubmatrix(matrix, k)
    print("\noutput:", serialize(ans, "integer"))