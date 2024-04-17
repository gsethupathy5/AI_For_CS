# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    tops: List[int] = deserialize("List[int]", read_line())
    bottoms: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minDominoRotations(tops, bottoms)
    print("\noutput:", serialize(ans, "integer"))
