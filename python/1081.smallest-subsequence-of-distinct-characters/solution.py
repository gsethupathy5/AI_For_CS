# Created by asetti2002 at 2024/04/25 20:00
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        
        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                stack.pop()
            stack.append(c)
        
        return ''.join(stack)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().smallestSubsequence(s)
    print("\noutput:", serialize(ans, "string"))
