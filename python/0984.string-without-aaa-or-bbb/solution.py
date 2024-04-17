# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/string-without-aaa-or-bbb/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    ans = Solution().strWithout3a3b(a, b)
    print("\noutput:", serialize(ans, "string"))
