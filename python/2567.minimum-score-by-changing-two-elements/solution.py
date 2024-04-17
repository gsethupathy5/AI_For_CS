# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-score-by-changing-two-elements/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimizeSum(nums)
    print("\noutput:", serialize(ans, "integer"))
