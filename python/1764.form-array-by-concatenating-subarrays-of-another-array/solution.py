# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    groups: List[List[int]] = deserialize("List[List[int]]", read_line())
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canChoose(groups, nums)
    print("\noutput:", serialize(ans, "boolean"))
