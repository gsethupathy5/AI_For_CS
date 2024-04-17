# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/satisfiability-of-equality-equations/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    equations: List[str] = deserialize("List[str]", read_line())
    ans = Solution().equationsPossible(equations)
    print("\noutput:", serialize(ans, "boolean"))
