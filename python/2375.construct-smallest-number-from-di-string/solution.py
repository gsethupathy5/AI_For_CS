# Created by asetti2002 at 2024/05/01 19:52
# leetgo: 1.4.3
# https://leetcode.com/problems/construct-smallest-number-from-di-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        stack = []
        for i in range(len(pattern)):
            if pattern[i] == 'I':
                stack.append(i)
                while stack:
                    res.append(stack.pop() + len(res) + 1)
            else:
                stack.append(i)
        stack.append(len(pattern))
        while stack:
            res.append(stack.pop() + len(res) + 1)
        return ''.join(str(num) for num in res)
# @lc code=end

if __name__ == "__main__":
    pattern: str = deserialize("str", read_line())
    ans = Solution().smallestNumber(pattern)
    print("\noutput:", serialize(ans, "string"))
