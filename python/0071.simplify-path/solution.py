# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/simplify-path/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def simplifyPath(self, path: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    path: str = deserialize("str", read_line())
    ans = Solution().simplifyPath(path)
    print("\noutput:", serialize(ans, "string"))