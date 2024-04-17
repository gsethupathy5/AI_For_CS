# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/intersection-of-multiple-arrays/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().intersection(nums)
    print("\noutput:", serialize(ans, "integer[]"))
