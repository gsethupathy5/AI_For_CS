# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/first-bad-version/

from typing import *
from leetgo_py import *

# @lc code=begin

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    bad: int = deserialize("int", read_line())
    ans = Solution().firstBadVersion(n, bad)
    print("\noutput:", serialize(ans, "integer"))
