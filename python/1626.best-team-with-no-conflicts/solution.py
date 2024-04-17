# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/best-team-with-no-conflicts/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    scores: List[int] = deserialize("List[int]", read_line())
    ages: List[int] = deserialize("List[int]", read_line())
    ans = Solution().bestTeamScore(scores, ages)
    print("\noutput:", serialize(ans, "integer"))
