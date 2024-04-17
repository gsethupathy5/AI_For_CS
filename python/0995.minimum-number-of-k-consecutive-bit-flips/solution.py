# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minKBitFlips(nums, k)
    print("\noutput:", serialize(ans, "integer"))
