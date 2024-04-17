# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    current: str = deserialize("str", read_line())
    correct: str = deserialize("str", read_line())
    ans = Solution().convertTime(current, correct)
    print("\noutput:", serialize(ans, "integer"))
