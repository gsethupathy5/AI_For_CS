# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().canPartitionKSubsets(nums, k)
    print("\noutput:", serialize(ans, "boolean"))
