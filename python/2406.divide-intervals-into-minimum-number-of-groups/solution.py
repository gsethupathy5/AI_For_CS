# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minGroups(intervals)
    print("\noutput:", serialize(ans, "integer"))