# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    operations: List[str] = deserialize("List[str]", read_line())
    ans = Solution().finalValueAfterOperations(operations)
    print("\noutput:", serialize(ans, "integer"))
