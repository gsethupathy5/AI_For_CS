# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    tokens: List[str] = deserialize("List[str]", read_line())
    ans = Solution().evalRPN(tokens)
    print("\noutput:", serialize(ans, "integer"))
