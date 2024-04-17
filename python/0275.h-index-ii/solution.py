# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/h-index-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    citations: List[int] = deserialize("List[int]", read_line())
    ans = Solution().hIndex(citations)
    print("\noutput:", serialize(ans, "integer"))
