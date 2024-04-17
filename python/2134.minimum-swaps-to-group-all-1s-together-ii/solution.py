# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minSwaps(nums)
    print("\noutput:", serialize(ans, "integer"))
