# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    text: str = deserialize("str", read_line())
    pattern: str = deserialize("str", read_line())
    ans = Solution().maximumSubsequenceCount(text, pattern)
    print("\noutput:", serialize(ans, "long"))
