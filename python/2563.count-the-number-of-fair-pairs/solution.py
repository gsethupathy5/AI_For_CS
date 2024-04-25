# Created by asetti2002 at 2024/04/18 18:06
# leetgo: 1.4.3
# https://leetcode.com/problems/count-the-number-of-fair-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    lower: int = deserialize("int", read_line())
    upper: int = deserialize("int", read_line())
    ans = Solution().countFairPairs(nums, lower, upper)
    print("\noutput:", serialize(ans, "long"))
