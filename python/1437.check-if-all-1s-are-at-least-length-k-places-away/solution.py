# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kLengthApart(nums, k)
    print("\noutput:", serialize(ans, "boolean"))
