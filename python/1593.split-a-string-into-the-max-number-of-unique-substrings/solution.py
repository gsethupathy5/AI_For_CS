# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maxUniqueSplit(s)
    print("\noutput:", serialize(ans, "integer"))
