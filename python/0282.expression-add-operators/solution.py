# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/expression-add-operators/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    num: str = deserialize("str", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().addOperators(num, target)
    print("\noutput:", serialize(ans, "string[]"))
