# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/grumpy-bookstore-owner/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    customers: List[int] = deserialize("List[int]", read_line())
    grumpy: List[int] = deserialize("List[int]", read_line())
    minutes: int = deserialize("int", read_line())
    ans = Solution().maxSatisfied(customers, grumpy, minutes)
    print("\noutput:", serialize(ans, "integer"))
