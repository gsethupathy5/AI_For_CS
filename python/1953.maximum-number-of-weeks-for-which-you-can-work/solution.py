# Created by asetti2002 at 2024/04/25 19:02
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        max_milestone = max(milestones)
        rest_sum = sum(milestones) - max_milestone
        
        if max_milestone <= rest_sum:
            return 2 * rest_sum + 1
        else:
            return rest_sum + rest_sum + max_milestone
# @lc code=end

if __name__ == "__main__":
    milestones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numberOfWeeks(milestones)
    print("\noutput:", serialize(ans, "long"))
