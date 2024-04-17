# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    firstLen: int = deserialize("int", read_line())
    secondLen: int = deserialize("int", read_line())
    ans = Solution().maxSumTwoNoOverlap(nums, firstLen, secondLen)
    print("\noutput:", serialize(ans, "integer"))
