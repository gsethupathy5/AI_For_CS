# Created by asetti2002 at 2024/05/01 20:04
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-distinct-averages/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # Write your code here
        pass
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().distinctAverages(nums)
    print("\noutput:", serialize(ans, "integer"))
