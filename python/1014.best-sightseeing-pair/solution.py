# Created by asetti2002 at 2024/04/25 19:54
# leetgo: 1.4.3
# https://leetcode.com/problems/best-sightseeing-pair/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = 0
        prev_best = values[0]
        for i in range(1, len(values)):
            max_score = max(max_score, prev_best + values[i] - i)
            prev_best = max(prev_best, values[i] + i)
        return max_score
# @lc code=end

if __name__ == "__main__":
    values: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxScoreSightseeingPair(values)
    print("\noutput:", serialize(ans, "integer"))
