# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-uncommon-subsequence-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findLUSlength(strs)
    print("\noutput:", serialize(ans, "integer"))
