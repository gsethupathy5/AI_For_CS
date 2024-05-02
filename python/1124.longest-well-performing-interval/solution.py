# Created by asetti2002 at 2024/04/25 20:03
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-well-performing-interval/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        stack = []
        res = score = 0
        for i, h in enumerate(hours):
            if h > 8:
                score += 1
            else:
                score -= 1
            if score > 0:
                res = i + 1
            if not stack or score < stack[-1][1]:
                stack.append((i, score))
        while stack:
            i, s = stack.pop()
            if s > 0:
                return max(res, i - stack[-1][0])
        return res
# @lc code=end

if __name__ == "__main__":
    hours: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestWPI(hours)
    print("\noutput:", serialize(ans, "integer"))
