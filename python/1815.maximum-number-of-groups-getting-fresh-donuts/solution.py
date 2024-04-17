# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    batchSize: int = deserialize("int", read_line())
    groups: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxHappyGroups(batchSize, groups)
    print("\noutput:", serialize(ans, "integer"))
