# Created by asetti2002 at 2024/05/01 20:13
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-cost-to-split-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        # Your code here
        pass
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minCost(nums, k)
    print("\noutput:", serialize(ans, "integer"))
