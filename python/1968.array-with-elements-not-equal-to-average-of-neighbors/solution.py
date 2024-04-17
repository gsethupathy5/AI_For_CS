# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().rearrangeArray(nums)
    print("\noutput:", serialize(ans, "integer[]"))
