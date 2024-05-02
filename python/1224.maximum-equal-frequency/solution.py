# Created by asetti2002 at 2024/04/25 20:19
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-equal-frequency/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxEqualFreq(nums)
    print("\noutput:", serialize(ans, "integer"))
