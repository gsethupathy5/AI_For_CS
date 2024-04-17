# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/daily-temperatures/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    temperatures: List[int] = deserialize("List[int]", read_line())
    ans = Solution().dailyTemperatures(temperatures)
    print("\noutput:", serialize(ans, "integer[]"))
