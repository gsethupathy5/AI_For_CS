# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kClosest(points, k)
    print("\noutput:", serialize(ans, "integer[][]"))
