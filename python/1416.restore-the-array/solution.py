# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/restore-the-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numberOfArrays(s, k)
    print("\noutput:", serialize(ans, "integer"))
