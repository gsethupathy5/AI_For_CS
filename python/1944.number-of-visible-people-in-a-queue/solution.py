# Created by asetti2002 at 2024/04/25 20:13
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-visible-people-in-a-queue/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and heights[i] > heights[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            if stack:
                ans[stack[-1]] += 1
            stack.append(i)
        return ans
# @lc code=end

if __name__ == "__main__":
    heights: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canSeePersonsCount(heights)
    print("\noutput:", serialize(ans, "integer[]"))
