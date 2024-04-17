# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().smallestRange(nums)
    print("\noutput:", serialize(ans, "integer[]"))
