# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().validPartition(nums)
    print("\noutput:", serialize(ans, "boolean"))
