# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/array-partition/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().arrayPairSum(nums)
    print("\noutput:", serialize(ans, "integer"))