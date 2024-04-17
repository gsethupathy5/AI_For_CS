# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/magnetic-force-between-two-balls/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    position: List[int] = deserialize("List[int]", read_line())
    m: int = deserialize("int", read_line())
    ans = Solution().maxDistance(position, m)
    print("\noutput:", serialize(ans, "integer"))
