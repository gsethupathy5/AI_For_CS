# Created by asetti2002 at 2024/04/25 19:44
# leetgo: 1.4.3
# https://leetcode.com/problems/validate-stack-sequences/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return len(stack) == 0
# @lc code=end

if __name__ == "__main__":
    pushed: List[int] = deserialize("List[int]", read_line())
    popped: List[int] = deserialize("List[int]", read_line())
    ans = Solution().validateStackSequences(pushed, popped)
    print("\noutput:", serialize(ans, "boolean"))
