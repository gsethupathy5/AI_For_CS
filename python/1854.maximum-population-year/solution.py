# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-population-year/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    logs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumPopulation(logs)
    print("\noutput:", serialize(ans, "integer"))
