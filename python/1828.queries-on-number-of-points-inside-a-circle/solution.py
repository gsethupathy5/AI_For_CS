# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPoints(points, queries)
    print("\noutput:", serialize(ans, "integer[]"))
