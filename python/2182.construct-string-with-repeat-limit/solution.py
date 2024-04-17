# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/construct-string-with-repeat-limit/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    repeatLimit: int = deserialize("int", read_line())
    ans = Solution().repeatLimitedString(s, repeatLimit)
    print("\noutput:", serialize(ans, "string"))
