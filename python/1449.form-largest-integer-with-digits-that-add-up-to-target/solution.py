# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    cost: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().largestNumber(cost, target)
    print("\noutput:", serialize(ans, "string"))
