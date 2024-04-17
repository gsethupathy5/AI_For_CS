# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    capacity: List[int] = deserialize("List[int]", read_line())
    rocks: List[int] = deserialize("List[int]", read_line())
    additionalRocks: int = deserialize("int", read_line())
    ans = Solution().maximumBags(capacity, rocks, additionalRocks)
    print("\noutput:", serialize(ans, "integer"))
