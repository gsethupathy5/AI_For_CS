# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/find-right-interval/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findRightInterval(intervals)
    print("\noutput:", serialize(ans, "integer[]"))
