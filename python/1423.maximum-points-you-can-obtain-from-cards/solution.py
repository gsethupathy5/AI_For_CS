# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    cardPoints: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxScore(cardPoints, k)
    print("\noutput:", serialize(ans, "integer"))
