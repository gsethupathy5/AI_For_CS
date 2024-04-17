# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-segment-sum-after-removals/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    removeQueries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumSegmentSum(nums, removeQueries)
    print("\noutput:", serialize(ans, "long[]"))
