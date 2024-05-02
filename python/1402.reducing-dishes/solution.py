# Created by asetti2002 at 2024/04/25 20:37
# leetgo: 1.4.3
# https://leetcode.com/problems/reducing-dishes/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        max_sum = 0
        total = 0
        
        for s in satisfaction:
            total += s
            if total > 0:
                max_sum += total
            else:
                break
        
        return max_sum
# @lc code=end

if __name__ == "__main__":
    satisfaction: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSatisfaction(satisfaction)
    print("\noutput:", serialize(ans, "integer"))
