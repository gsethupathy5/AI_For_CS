# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    grades: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumGroups(grades)
    print("\noutput:", serialize(ans, "integer"))