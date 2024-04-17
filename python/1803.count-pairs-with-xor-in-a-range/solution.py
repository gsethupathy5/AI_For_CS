# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    low: int = deserialize("int", read_line())
    high: int = deserialize("int", read_line())
    ans = Solution().countPairs(nums, low, high)
    print("\noutput:", serialize(ans, "integer"))
