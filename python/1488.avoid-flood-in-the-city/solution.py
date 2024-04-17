# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/avoid-flood-in-the-city/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    rains: List[int] = deserialize("List[int]", read_line())
    ans = Solution().avoidFlood(rains)
    print("\noutput:", serialize(ans, "integer[]"))
