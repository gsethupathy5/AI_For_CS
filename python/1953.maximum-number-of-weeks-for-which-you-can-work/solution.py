# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    milestones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numberOfWeeks(milestones)
    print("\noutput:", serialize(ans, "long"))
