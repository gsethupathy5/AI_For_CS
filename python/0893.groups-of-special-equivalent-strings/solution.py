# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/groups-of-special-equivalent-strings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().numSpecialEquivGroups(words)
    print("\noutput:", serialize(ans, "integer"))
