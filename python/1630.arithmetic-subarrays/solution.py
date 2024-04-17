# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/arithmetic-subarrays/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    l: List[int] = deserialize("List[int]", read_line())
    r: List[int] = deserialize("List[int]", read_line())
    ans = Solution().checkArithmeticSubarrays(nums, l, r)
    print("\noutput:", serialize(ans, "boolean[]"))
