# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/count-lattice-points-inside-a-circle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    circles: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countLatticePoints(circles)
    print("\noutput:", serialize(ans, "integer"))
