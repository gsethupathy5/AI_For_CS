# Created by asetti2002 at 2024/04/25 19:34
# leetgo: 1.4.3
# https://leetcode.com/problems/decoded-string-at-index/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for c in s:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
        for c in reversed(s):
            k %= size
            if k == 0 and c.isalpha():
                return c
            if c.isdigit():
                size /= int(c)
            else:
                size -= 1
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().decodeAtIndex(s, k)
    print("\noutput:", serialize(ans, "string"))
