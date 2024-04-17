# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    seq: str = deserialize("str", read_line())
    ans = Solution().maxDepthAfterSplit(seq)
    print("\noutput:", serialize(ans, "integer[]"))
