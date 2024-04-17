# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().averageValue(nums)
    print("\noutput:", serialize(ans, "integer"))
