# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-xor-for-each-query/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    maximumBit: int = deserialize("int", read_line())
    ans = Solution().getMaximumXor(nums, maximumBit)
    print("\noutput:", serialize(ans, "integer[]"))
