# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().smallerNumbersThanCurrent(nums)
    print("\noutput:", serialize(ans, "integer[]"))
