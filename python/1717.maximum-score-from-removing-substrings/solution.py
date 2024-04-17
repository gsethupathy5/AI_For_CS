# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-score-from-removing-substrings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    ans = Solution().maximumGain(s, x, y)
    print("\noutput:", serialize(ans, "integer"))
