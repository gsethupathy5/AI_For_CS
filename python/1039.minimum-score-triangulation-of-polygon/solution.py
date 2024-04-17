# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    values: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minScoreTriangulation(values)
    print("\noutput:", serialize(ans, "integer"))
