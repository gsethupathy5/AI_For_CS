# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/generate-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().generateParenthesis(n)
    print("\noutput:", serialize(ans, "string[]"))
