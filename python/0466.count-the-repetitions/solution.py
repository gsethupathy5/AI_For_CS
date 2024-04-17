# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/count-the-repetitions/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    n1: int = deserialize("int", read_line())
    s2: str = deserialize("str", read_line())
    n2: int = deserialize("int", read_line())
    ans = Solution().getMaxRepetitions(s1, n1, s2, n2)
    print("\noutput:", serialize(ans, "integer"))
