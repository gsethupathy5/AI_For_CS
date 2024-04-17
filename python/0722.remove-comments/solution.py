# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-comments/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    source: List[str] = deserialize("List[str]", read_line())
    ans = Solution().removeComments(source)
    print("\noutput:", serialize(ans, "string[]"))
