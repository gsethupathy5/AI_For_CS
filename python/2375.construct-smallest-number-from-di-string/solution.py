# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/construct-smallest-number-from-di-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    pattern: str = deserialize("str", read_line())
    ans = Solution().smallestNumber(pattern)
    print("\noutput:", serialize(ans, "string"))