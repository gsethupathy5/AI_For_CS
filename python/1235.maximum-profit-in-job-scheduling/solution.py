# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    startTime: List[int] = deserialize("List[int]", read_line())
    endTime: List[int] = deserialize("List[int]", read_line())
    profit: List[int] = deserialize("List[int]", read_line())
    ans = Solution().jobScheduling(startTime, endTime, profit)
    print("\noutput:", serialize(ans, "integer"))
