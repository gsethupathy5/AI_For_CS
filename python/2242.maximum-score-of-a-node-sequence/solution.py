# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-score-of-a-node-sequence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    scores: List[int] = deserialize("List[int]", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumScore(scores, edges)
    print("\noutput:", serialize(ans, "integer"))
