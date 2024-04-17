# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/unique-binary-search-trees/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numTrees(self, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().numTrees(n)
    print("\noutput:", serialize(ans, "integer"))
