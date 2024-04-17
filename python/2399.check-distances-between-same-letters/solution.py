# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/check-distances-between-same-letters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    distance: List[int] = deserialize("List[int]", read_line())
    ans = Solution().checkDistances(s, distance)
    print("\noutput:", serialize(ans, "boolean"))
