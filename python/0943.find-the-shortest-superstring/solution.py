# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-shortest-superstring/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().shortestSuperstring(words)
    print("\noutput:", serialize(ans, "string"))
