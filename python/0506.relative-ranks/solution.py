# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/relative-ranks/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    score: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findRelativeRanks(score)
    print("\noutput:", serialize(ans, "string[]"))
