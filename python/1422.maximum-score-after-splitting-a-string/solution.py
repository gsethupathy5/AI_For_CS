# Created by asetti2002 at 2024/04/25 20:42
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            score = left.count('0') + right.count('1')
            max_score = max(max_score, score)
        return max_score
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maxScore(s)
    print("\noutput:", serialize(ans, "integer"))
