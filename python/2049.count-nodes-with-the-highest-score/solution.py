# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/count-nodes-with-the-highest-score/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    parents: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countHighestScoreNodes(parents)
    print("\noutput:", serialize(ans, "integer"))
