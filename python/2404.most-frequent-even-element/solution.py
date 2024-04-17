# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/most-frequent-even-element/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().mostFrequentEven(nums)
    print("\noutput:", serialize(ans, "integer"))
