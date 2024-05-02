# Created by asetti2002 at 2024/04/25 20:41
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-a-string-can-break-another-string/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)
        return all(a >= b for a, b in zip(s1_sorted, s2_sorted)) or all(a >= b for a, b in zip(s2_sorted, s1_sorted))
# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    ans = Solution().checkIfCanBreak(s1, s2)
    print("\noutput:", serialize(ans, "boolean"))
