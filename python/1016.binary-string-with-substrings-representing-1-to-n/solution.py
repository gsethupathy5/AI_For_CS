# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().queryString(s, n)
    print("\noutput:", serialize(ans, "boolean"))
