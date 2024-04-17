# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-atoms/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    formula: str = deserialize("str", read_line())
    ans = Solution().countOfAtoms(formula)
    print("\noutput:", serialize(ans, "string"))
