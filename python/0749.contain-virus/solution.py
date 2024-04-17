# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/contain-virus/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    isInfected: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().containVirus(isInfected)
    print("\noutput:", serialize(ans, "integer"))
