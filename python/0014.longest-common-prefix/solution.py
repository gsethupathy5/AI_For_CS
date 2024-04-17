# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-common-prefix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().longestCommonPrefix(strs)
    print("\noutput:", serialize(ans, "string"))
