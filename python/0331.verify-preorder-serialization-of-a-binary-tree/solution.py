# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    preorder: str = deserialize("str", read_line())
    ans = Solution().isValidSerialization(preorder)
    print("\noutput:", serialize(ans, "boolean"))
