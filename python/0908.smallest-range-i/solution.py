# Created by asetti2002 at 2024/04/25 19:38
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-range-i/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2*k)
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().smallestRangeI(nums, k)
    print("\noutput:", serialize(ans, "integer"))
