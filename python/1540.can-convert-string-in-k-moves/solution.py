# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/can-convert-string-in-k-moves/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().canConvertString(s, t, k)
    print("\noutput:", serialize(ans, "boolean"))
