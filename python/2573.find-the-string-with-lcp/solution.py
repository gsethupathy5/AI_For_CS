# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-string-with-lcp/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    lcp: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findTheString(lcp)
    print("\noutput:", serialize(ans, "string"))
