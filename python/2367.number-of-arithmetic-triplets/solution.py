# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-arithmetic-triplets/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    diff: int = deserialize("int", read_line())
    ans = Solution().arithmeticTriplets(nums, diff)
    print("\noutput:", serialize(ans, "integer"))
