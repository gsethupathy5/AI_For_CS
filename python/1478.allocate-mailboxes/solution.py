# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/allocate-mailboxes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    houses: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minDistance(houses, k)
    print("\noutput:", serialize(ans, "integer"))
