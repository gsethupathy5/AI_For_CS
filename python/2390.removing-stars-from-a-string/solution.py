# Created by asetti2002 at 2024/05/01 19:54
# leetgo: 1.4.3
# https://leetcode.com/problems/removing-stars-from-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().removeStars(s)
    print("\noutput:", serialize(ans, "string"))
