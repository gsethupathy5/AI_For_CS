# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    n: int = deserialize("int", read_line())
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().rangeSum(nums, n, left, right)
    print("\noutput:", serialize(ans, "integer"))
