# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/build-a-matrix-with-conditions/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    rowConditions: List[List[int]] = deserialize("List[List[int]]", read_line())
    colConditions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().buildMatrix(k, rowConditions, colConditions)
    print("\noutput:", serialize(ans, "integer[][]"))
