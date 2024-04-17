# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-good-people-based-on-statements/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    statements: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumGood(statements)
    print("\noutput:", serialize(ans, "integer"))
