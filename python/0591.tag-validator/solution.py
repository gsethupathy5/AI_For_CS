# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/tag-validator/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isValid(self, code: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    code: str = deserialize("str", read_line())
    ans = Solution().isValid(code)
    print("\noutput:", serialize(ans, "boolean"))
