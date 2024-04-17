# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/max-value-of-equation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findMaxValueOfEquation(points, k)
    print("\noutput:", serialize(ans, "integer"))
