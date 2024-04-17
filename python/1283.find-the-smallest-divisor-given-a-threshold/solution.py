# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    threshold: int = deserialize("int", read_line())
    ans = Solution().smallestDivisor(nums, threshold)
    print("\noutput:", serialize(ans, "integer"))
