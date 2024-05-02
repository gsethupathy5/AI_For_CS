# Created by asetti2002 at 2024/04/25 20:27
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minFlips(mat)
    print("\noutput:", serialize(ans, "integer"))
