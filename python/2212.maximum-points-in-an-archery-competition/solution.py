# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-points-in-an-archery-competition/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    numArrows: int = deserialize("int", read_line())
    aliceArrows: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumBobPoints(numArrows, aliceArrows)
    print("\noutput:", serialize(ans, "integer[]"))
