# Created by asetti2002 at 2024/05/01 20:15
# leetgo: 1.4.3
# https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().beautifulSubarrays(nums)
    print("\noutput:", serialize(ans, "long"))
