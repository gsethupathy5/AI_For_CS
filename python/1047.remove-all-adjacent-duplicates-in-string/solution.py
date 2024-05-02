# Created by asetti2002 at 2024/04/25 19:58
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().removeDuplicates(s)
    print("\noutput:", serialize(ans, "string"))
